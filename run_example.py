#!/usr/bin/env python3
"""
Example script showing how to use the Google Drive Statement Organizer
"""

import os
import sys
from pathlib import Path

def main():
    """Example usage of the Google Drive Statement Organizer."""
    
    print("Google Drive Statement Organizer - Example Usage")
    print("=" * 50)
    
    # Check if credentials file exists
    if not os.path.exists('credentials.json'):
        print("\n❌ credentials.json not found!")
        print("\nTo get started:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a new project or select existing one")
        print("3. Enable Google Drive API")
        print("4. Create OAuth 2.0 credentials (Desktop application)")
        print("5. Download the JSON file and rename it to 'credentials.json'")
        print("6. Place it in this directory")
        print("\nSee setup_instructions.md for detailed steps.")
        return 1
    
    print("✅ credentials.json found")
    
    # Example commands
    print("\n📋 Example Commands:")
    print("\n1. Dry run (preview changes without making them):")
    print("   python main.py --dry-run")
    
    print("\n2. Run with default folder names:")
    print("   python main.py")
    
    print("\n3. Run with custom folder names:")
    print("   python main.py --monthly-statements 'My Statements' --statements-by-account 'Organized'")
    
    print("\n4. Run with specific folder IDs:")
    print("   python main.py --source-folder-id '1ABC123...' --dest-folder-id '1XYZ789...'")
    
    print("\n5. Run with custom credentials file:")
    print("   python main.py --credentials-file 'my_credentials.json'")
    
    print("\n📁 Expected Folder Structure:")
    print("Google Drive:")
    print("├── Monthly Statements/          (source folder)")
    print("│   ├── chase_bank_statement.pdf")
    print("│   ├── amex_credit_card.pdf")
    print("│   └── fidelity_investment.pdf")
    print("└── Statements by Account/       (destination folder)")
    print("    ├── chase/")
    print("    │   └── bank statement/")
    print("    ├── american express/")
    print("    │   └── credit card statement/")
    print("    └── fidelity/")
    print("        └── investment statement/")
    
    print("\n🔧 Supported Companies:")
    companies = [
        "Chase", "Wells Fargo", "Bank of America", "American Express",
        "Capital One", "Citi", "Fidelity", "Vanguard", "Schwab",
        "PayPal", "Stripe", "Coinbase", "Robinhood"
    ]
    for company in companies:
        print(f"   • {company}")
    
    print("\n📄 Supported Statement Types:")
    types = [
        "Bank Statement", "Credit Card Statement", "Investment Statement",
        "Loan Statement", "Insurance Statement", "Utility Statement"
    ]
    for stmt_type in types:
        print(f"   • {stmt_type}")
    
    print("\n🚀 Ready to run? Try:")
    print("   python main.py --dry-run")
    
    return 0


if __name__ == '__main__':
    exit(main())
