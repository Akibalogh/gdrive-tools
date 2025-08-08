#!/usr/bin/env python3
"""
Google Drive Statement Organizer

This application organizes financial statements from a "Monthly Statements" folder
into a structured "Statements by Account" folder based on company names and statement types.
"""

import os
import re
import json
import logging
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import tempfile

import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from dotenv import load_dotenv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

import PyPDF2
import io

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Initialize Rich console
console = Console()


class GoogleDriveOrganizer:
    """Main class for organizing Google Drive statements."""
    
    def __init__(self, credentials_file: str = 'credentials.json', token_file: str = 'token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.service = None
        self.authenticate()
    
    def authenticate(self):
        """Authenticate with Google Drive API."""
        creds = None
        
        # Load existing token
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        
        # If no valid credentials, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    console.print(f"[red]Error: {self.credentials_file} not found. Please download your OAuth credentials from Google Cloud Console.[/red]")
                    raise FileNotFoundError(f"Credentials file {self.credentials_file} not found")
                
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for next run
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('drive', 'v3', credentials=creds)
        console.print("[green]✓ Successfully authenticated with Google Drive[/green]")
    
    def find_folder_by_name(self, folder_name: str, parent_id: Optional[str] = None) -> Optional[str]:
        """Find a folder by name and optionally parent folder ID."""
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
        if parent_id:
            query += f" and '{parent_id}' in parents"
        
        try:
            results = self.service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
            files = results.get('files', [])
            
            if files:
                return files[0]['id']
            else:
                console.print(f"[yellow]Warning: Folder '{folder_name}' not found[/yellow]")
                return None
        except HttpError as error:
            console.print(f"[red]Error finding folder '{folder_name}': {error}[/red]")
            return None
    
    def get_files_in_folder(self, folder_id: str) -> List[Dict]:
        """Get all files in a folder."""
        try:
            results = self.service.files().list(
                q=f"'{folder_id}' in parents and trashed=false",
                spaces='drive',
                fields='files(id, name, mimeType, size)'
            ).execute()
            return results.get('files', [])
        except HttpError as error:
            console.print(f"[red]Error getting files from folder: {error}[/red]")
            return []
    
    def create_folder(self, folder_name: str, parent_id: Optional[str] = None) -> Optional[str]:
        """Create a folder in Google Drive."""
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        
        if parent_id:
            file_metadata['parents'] = [parent_id]
        
        try:
            folder = self.service.files().create(body=file_metadata, fields='id').execute()
            console.print(f"[green]✓ Created folder: {folder_name}[/green]")
            return folder.get('id')
        except HttpError as error:
            console.print(f"[red]Error creating folder '{folder_name}': {error}[/red]")
            return None
    
    def download_file(self, file_id: str) -> Optional[bytes]:
        """Download a file from Google Drive."""
        try:
            request = self.service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            return file.getvalue()
        except HttpError as error:
            console.print(f"[red]Error downloading file: {error}[/red]")
            return None
    
    def copy_file(self, file_id: str, destination_folder_id: str, new_name: Optional[str] = None) -> bool:
        """Copy a file to a new location in Google Drive."""
        try:
            # Get file metadata
            file_metadata = self.service.files().get(fileId=file_id).execute()
            
            # Prepare copy metadata
            copy_metadata = {
                'name': new_name or file_metadata['name'],
                'parents': [destination_folder_id]
            }
            
            # Copy the file
            copied_file = self.service.files().copy(
                fileId=file_id,
                body=copy_metadata
            ).execute()
            
            console.print(f"[green]✓ Copied: {copy_metadata['name']}[/green]")
            return True
        except HttpError as error:
            console.print(f"[red]Error copying file: {error}[/red]")
            return False
    
    def extract_text_from_pdf(self, pdf_content: bytes) -> str:
        """Extract text content from PDF bytes."""
        try:
            pdf_file = io.BytesIO(pdf_content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            return text
        except Exception as e:
            console.print(f"[yellow]Warning: Could not extract text from PDF: {e}[/yellow]")
            return ""
    
    def classify_file(self, file_name: str, file_content: Optional[bytes] = None) -> Tuple[Optional[str], Optional[str]]:
        """Classify a file based on filename and optionally content."""
        company = None
        statement_type = None
        
        # Import patterns from config
        from config import COMPANY_PATTERNS, STATEMENT_PATTERNS
        
        # Analyze filename
        file_lower = file_name.lower()
        
        # Find company
        for company_name, patterns in COMPANY_PATTERNS.items():
            if any(pattern in file_lower for pattern in patterns):
                company = company_name
                break
        
        # Find statement type
        for stmt_type, patterns in STATEMENT_PATTERNS.items():
            if any(pattern in file_lower for pattern in patterns):
                statement_type = stmt_type
                break
        
        # If filename analysis didn't work, try PDF content
        if (not company or not statement_type) and file_content:
            pdf_text = self.extract_text_from_pdf(file_content)
            pdf_lower = pdf_text.lower()
            
            # Find company in PDF content
            if not company:
                for company_name, patterns in COMPANY_PATTERNS.items():
                    if any(pattern in pdf_lower for pattern in patterns):
                        company = company_name
                        break
            
            # Find statement type in PDF content
            if not statement_type:
                for stmt_type, patterns in STATEMENT_PATTERNS.items():
                    if any(pattern in pdf_lower for pattern in patterns):
                        statement_type = stmt_type
                        break
        
        return company, statement_type
    
    def organize_statements(self, source_folder_id: str, dest_folder_id: str, dry_run: bool = False) -> Dict:
        """Organize statements from source folder to destination folder."""
        console.print(f"\n[bold blue]Starting statement organization...[/bold blue]")
        
        # Get files from source folder
        files = self.get_files_in_folder(source_folder_id)
        
        if not files:
            console.print("[yellow]No files found in source folder[/yellow]")
            return {}
        
        console.print(f"Found {len(files)} files to process")
        
        # Statistics
        stats = {
            'total_files': len(files),
            'processed': 0,
            'copied': 0,
            'skipped': 0,
            'errors': 0,
            'unclassified': 0
        }
        
        # Process each file
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Processing files...", total=len(files))
            
            for file in files:
                progress.update(task, description=f"Processing: {file['name']}")
                
                try:
                    # Skip non-PDF files for now
                    if not file['name'].lower().endswith('.pdf'):
                        console.print(f"[yellow]Skipping non-PDF file: {file['name']}[/yellow]")
                        stats['skipped'] += 1
                        progress.advance(task)
                        continue
                    
                    # Download file content for analysis
                    file_content = self.download_file(file['id'])
                    
                    # Classify the file
                    company, statement_type = self.classify_file(file['name'], file_content)
                    
                    if not company or not statement_type:
                        console.print(f"[yellow]Could not classify: {file['name']}[/yellow]")
                        stats['unclassified'] += 1
                        progress.advance(task)
                        continue
                    
                    # Create folder structure if needed
                    company_folder_id = self.find_folder_by_name(company, dest_folder_id)
                    if not company_folder_id:
                        if not dry_run:
                            company_folder_id = self.create_folder(company, dest_folder_id)
                        else:
                            console.print(f"[blue]Would create folder: {company}[/blue]")
                    
                    if company_folder_id:
                        statement_folder_id = self.find_folder_by_name(statement_type, company_folder_id)
                        if not statement_folder_id:
                            if not dry_run:
                                statement_folder_id = self.create_folder(statement_type, company_folder_id)
                            else:
                                console.print(f"[blue]Would create folder: {company}/{statement_type}[/blue]")
                        
                        # Copy file to destination
                        if statement_folder_id and not dry_run:
                            success = self.copy_file(file['id'], statement_folder_id)
                            if success:
                                stats['copied'] += 1
                            else:
                                stats['errors'] += 1
                        elif dry_run:
                            console.print(f"[blue]Would copy: {file['name']} → {company}/{statement_type}/[/blue]")
                            stats['copied'] += 1
                    
                    stats['processed'] += 1
                    
                except Exception as e:
                    console.print(f"[red]Error processing {file['name']}: {e}[/red]")
                    stats['errors'] += 1
                
                progress.advance(task)
        
        return stats


@click.command()
@click.option('--source-folder-id', envvar='SOURCE_FOLDER_ID', help='Google Drive folder ID for source folder')
@click.option('--dest-folder-id', envvar='DEST_FOLDER_ID', help='Google Drive folder ID for destination folder')
@click.option('--credentials-file', default='credentials.json', help='Path to Google API credentials file')
@click.option('--dry-run', is_flag=True, help='Preview changes without making them')
@click.option('--monthly-statements', default='Monthly Statements', help='Name of monthly statements folder')
@click.option('--statements-by-account', default='Statements by Account', help='Name of statements by account folder')
def main(source_folder_id: str, dest_folder_id: str, credentials_file: str, dry_run: bool, 
         monthly_statements: str, statements_by_account: str):
    """Organize Google Drive statements by company and type."""
    
    console.print("[bold green]Google Drive Statement Organizer[/bold green]")
    
    if dry_run:
        console.print("[yellow]Running in DRY RUN mode - no changes will be made[/yellow]")
    
    # Initialize organizer
    try:
        organizer = GoogleDriveOrganizer(credentials_file)
    except Exception as e:
        console.print(f"[red]Failed to initialize: {e}[/red]")
        return 1
    
    # Find folders if IDs not provided
    if not source_folder_id:
        console.print(f"Looking for '{monthly_statements}' folder...")
        source_folder_id = organizer.find_folder_by_name(monthly_statements)
        if not source_folder_id:
            console.print(f"[red]Could not find '{monthly_statements}' folder[/red]")
            return 1
    
    if not dest_folder_id:
        console.print(f"Looking for '{statements_by_account}' folder...")
        dest_folder_id = organizer.find_folder_by_name(statements_by_account)
        if not dest_folder_id:
            console.print(f"[red]Could not find '{statements_by_account}' folder[/red]")
            return 1
    
    # Organize statements
    stats = organizer.organize_statements(source_folder_id, dest_folder_id, dry_run)
    
    # Display results
    console.print(f"\n[bold blue]Organization Complete![/bold blue]")
    
    table = Table(title="Processing Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Count", style="magenta")
    
    table.add_row("Total Files", str(stats['total_files']))
    table.add_row("Processed", str(stats['processed']))
    table.add_row("Copied", str(stats['copied']))
    table.add_row("Skipped", str(stats['skipped']))
    table.add_row("Unclassified", str(stats['unclassified']))
    table.add_row("Errors", str(stats['errors']))
    
    console.print(table)
    
    return 0


if __name__ == '__main__':
    exit(main())
