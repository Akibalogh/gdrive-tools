#!/usr/bin/env python3
"""
Tests for Google Drive Statement Organizer
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import tempfile
import os
import io

from main import GoogleDriveOrganizer


class TestGoogleDriveOrganizer(unittest.TestCase):
    """Test cases for GoogleDriveOrganizer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Mock the authentication to avoid requiring real credentials
        with patch.object(GoogleDriveOrganizer, 'authenticate'):
            self.organizer = GoogleDriveOrganizer()
            self.organizer.service = Mock()
    
    def test_classify_file_bank_statement(self):
        """Test classification of bank statement files."""
        filename = "chase_bank_statement_january_2024.pdf"
        company, statement_type, account_info = self.organizer.classify_file(filename)
        
        self.assertEqual(company, "chase")
        self.assertEqual(statement_type, "bank statement")
        self.assertIsNone(account_info)  # No account info in this filename
    
    def test_classify_file_credit_card(self):
        """Test classification of credit card statement files."""
        filename = "amex_credit_card_statement_february_2024.pdf"
        company, statement_type, account_info = self.organizer.classify_file(filename)
        
        self.assertEqual(company, "american express")
        self.assertEqual(statement_type, "credit card statement")
        self.assertIsNone(account_info)  # No account info in this filename
    
    def test_classify_file_investment(self):
        """Test classification of investment statement files."""
        filename = "fidelity_investment_statement_march_2024.pdf"
        company, statement_type, account_info = self.organizer.classify_file(filename)
        
        self.assertEqual(company, "fidelity")
        self.assertEqual(statement_type, "investment statement")
        self.assertIsNone(account_info)  # No account info in this filename
    
    def test_classify_file_with_account_info(self):
        """Test classification with account information."""
        filename = "schwab_investment_statement_account_1234-5678.pdf"
        company, statement_type, account_info = self.organizer.classify_file(filename)
        
        self.assertEqual(company, "schwab")
        self.assertEqual(statement_type, "investment statement")
        self.assertEqual(account_info, "1234-5678")
    
    def test_classify_file_unknown_company(self):
        """Test classification with unknown company."""
        filename = "unknown_company_statement.pdf"
        company, statement_type, account_info = self.organizer.classify_file(filename)
        
        self.assertIsNone(company)
        self.assertIsNone(statement_type)
        self.assertIsNone(account_info)
    
    def test_extract_text_from_pdf(self):
        """Test PDF text extraction."""
        # Create a simple PDF-like content for testing
        pdf_content = b"%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n"
        
        with patch('PyPDF2.PdfReader') as mock_reader:
            mock_page = Mock()
            mock_page.extract_text.return_value = "Sample PDF content"
            mock_reader.return_value.pages = [mock_page]
            
            text = self.organizer.extract_text_from_pdf(pdf_content)
            self.assertEqual(text, "Sample PDF content\n")
    
    def test_find_folder_by_name(self):
        """Test finding folder by name."""
        mock_response = {
            'files': [{'id': 'test_folder_id', 'name': 'Test Folder'}]
        }
        self.organizer.service.files().list().execute.return_value = mock_response
        
        folder_id = self.organizer.find_folder_by_name('Test Folder')
        self.assertEqual(folder_id, 'test_folder_id')
    
    def test_find_folder_by_name_not_found(self):
        """Test finding folder that doesn't exist."""
        mock_response = {'files': []}
        self.organizer.service.files().list().execute.return_value = mock_response
        
        folder_id = self.organizer.find_folder_by_name('Non-existent Folder')
        self.assertIsNone(folder_id)
    
    def test_get_files_in_folder(self):
        """Test getting files from a folder."""
        mock_response = {
            'files': [
                {'id': 'file1', 'name': 'statement1.pdf', 'mimeType': 'application/pdf'},
                {'id': 'file2', 'name': 'statement2.pdf', 'mimeType': 'application/pdf'}
            ]
        }
        self.organizer.service.files().list().execute.return_value = mock_response
        
        files = self.organizer.get_files_in_folder('test_folder_id')
        self.assertEqual(len(files), 2)
        self.assertEqual(files[0]['name'], 'statement1.pdf')
    
    def test_create_folder(self):
        """Test creating a new folder."""
        mock_response = {'id': 'new_folder_id'}
        self.organizer.service.files().create().execute.return_value = mock_response
        
        folder_id = self.organizer.create_folder('New Folder')
        self.assertEqual(folder_id, 'new_folder_id')
    
    def test_copy_file(self):
        """Test copying a file."""
        mock_file_metadata = {'name': 'test_file.pdf'}
        mock_copy_response = {'id': 'copied_file_id'}
        
        self.organizer.service.files().get().execute.return_value = mock_file_metadata
        self.organizer.service.files().copy().execute.return_value = mock_copy_response
        
        success = self.organizer.copy_file('source_file_id', 'dest_folder_id')
        self.assertTrue(success)


class TestFileClassification(unittest.TestCase):
    """Test cases for file classification logic."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Mock the authentication to avoid requiring real credentials
        with patch.object(GoogleDriveOrganizer, 'authenticate'):
            self.organizer = GoogleDriveOrganizer()
    
    def test_company_patterns(self):
        """Test various company name patterns."""
        test_cases = [
            ("chase_statement.pdf", "chase"),
            ("jpmorgan_statement.pdf", "chase"),
            ("wells_fargo_statement.pdf", "wells fargo"),
            ("bank_of_america_statement.pdf", "bank of america"),
            ("amex_statement.pdf", "american express"),
            ("fidelity_statement.pdf", "fidelity"),
            ("vanguard_statement.pdf", "vanguard"),
        ]
        
        for filename, expected_company in test_cases:
            with self.subTest(filename=filename):
                company, _, _ = self.organizer.classify_file(filename)
                self.assertEqual(company, expected_company)
    
    def test_statement_type_patterns(self):
        """Test various statement type patterns."""
        test_cases = [
            ("bank_statement.pdf", "bank statement"),
            ("credit_card_statement.pdf", "credit card statement"),
            ("investment_statement.pdf", "investment statement"),
            ("loan_statement.pdf", "loan statement"),
            ("insurance_statement.pdf", "insurance statement"),
            ("utility_statement.pdf", "utility statement"),
        ]
        
        for filename, expected_type in test_cases:
            with self.subTest(filename=filename):
                _, statement_type, _ = self.organizer.classify_file(filename)
                self.assertEqual(statement_type, expected_type)
    
    def test_debug_classification(self):
        """Debug test to see what's happening with classification."""
        filename = "chase_bank_statement.pdf"
        company, statement_type, account_info = self.organizer.classify_file(filename)
        print(f"Debug: filename='{filename}', company='{company}', statement_type='{statement_type}', account_info='{account_info}'")
        
        # This should help us understand what's happening
        self.assertIsNotNone(company, f"Company should be found for {filename}")
        self.assertIsNotNone(statement_type, f"Statement type should be found for {filename}")


if __name__ == '__main__':
    unittest.main()
