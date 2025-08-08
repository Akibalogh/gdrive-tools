# Google Drive Statement Organizer

This application helps organize financial statements from a "Monthly Statements" folder into a structured "Statements by Account" folder based on company names and statement types.

## Features

- Authenticates with Google Drive API using OAuth2
- Reads files from "Monthly Statements" folder
- Analyzes filenames and PDF contents to determine company and statement type
- Creates organized folder structure in "Statements by Account"
- Copies files to appropriate subfolders
- Supports both filename-based and content-based classification

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Google Drive API:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable Google Drive API
   - Create OAuth 2.0 credentials
   - Download the credentials JSON file

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Google Drive folder IDs and credentials path
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## Configuration

The app expects these folder structure:
- **Source:** "Monthly Statements" folder containing mixed statement files
- **Destination:** "Statements by Account" folder with subfolders for each company/account

## Usage

```bash
# Run with default settings
python main.py

# Run with custom folder IDs
python main.py --source-folder-id <ID> --dest-folder-id <ID>

# Dry run (preview changes without making them)
python main.py --dry-run
```

## File Classification

The app uses multiple strategies to classify files:

1. **Filename Analysis:** Looks for company names and statement types in filenames
2. **PDF Content Analysis:** Reads PDF text to extract company and statement information
3. **Pattern Matching:** Uses regex patterns to identify common statement formats

## Folder Structure

```
Statements by Account/
├── Company A/
│   ├── Bank Statements/
│   ├── Credit Card Statements/
│   └── Investment Statements/
├── Company B/
│   ├── Bank Statements/
│   └── Credit Card Statements/
└── ...
```
