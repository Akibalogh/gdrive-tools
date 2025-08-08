# Setup Instructions for Google Drive Statement Organizer

## Prerequisites

1. Python 3.8 or higher
2. Google account with access to Google Drive
3. Google Cloud Console access

## Step 1: Set up Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Drive API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Drive API"
   - Click on it and press "Enable"

## Step 2: Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client IDs"
3. Choose "Desktop application" as the application type
4. Give it a name (e.g., "Google Drive Statement Organizer")
5. Click "Create"
6. Download the JSON credentials file
7. Rename it to `credentials.json` and place it in the project root directory

## Step 3: Set up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Step 4: Configure Environment Variables

Create a `.env` file in the project root with the following content:

```env
# Google Drive API Configuration
GOOGLE_CREDENTIALS_FILE=credentials.json
GOOGLE_TOKEN_FILE=token.json

# Google Drive Folder IDs (optional - will be auto-detected if not provided)
SOURCE_FOLDER_ID=
MONTHLY_STATEMENTS_FOLDER_ID=
STATEMENTS_BY_ACCOUNT_FOLDER_ID=

# Application Settings
DRY_RUN=false
LOG_LEVEL=INFO
MAX_FILES_PER_RUN=100
```

## Step 5: First Run

1. Make sure your virtual environment is activated
2. Run the application:

```bash
# Test run (preview changes without making them)
python main.py --dry-run

# Actual run
python main.py
```

3. On first run, you'll be prompted to authenticate with Google:
   - A browser window will open
   - Sign in with your Google account (aki@antifragile.llc)
   - Grant permissions to access Google Drive
   - The authentication token will be saved for future runs

## Step 6: Folder Structure

The application expects these folders in your Google Drive:

- **Source Folder**: "Monthly Statements" (or custom name)
  - Contains mixed statement files (PDFs)
  
- **Destination Folder**: "Statements by Account" (or custom name)
  - Will be created automatically with subfolders for each company

## Usage Examples

```bash
# Basic usage
python main.py

# Dry run to preview changes
python main.py --dry-run

# Specify custom folder names
python main.py --monthly-statements "My Statements" --statements-by-account "Organized Statements"

# Use specific folder IDs
python main.py --source-folder-id "1ABC123..." --dest-folder-id "1XYZ789..."

# Specify custom credentials file
python main.py --credentials-file "my_credentials.json"
```

## Troubleshooting

### Authentication Issues
- Make sure `credentials.json` is in the project root
- Delete `token.json` and re-authenticate if you get permission errors
- Ensure the Google Drive API is enabled in your Google Cloud project

### Folder Not Found
- Check that the folder names match exactly (case-sensitive)
- Verify you have access to the folders in Google Drive
- Use folder IDs instead of names if needed

### File Classification Issues
- The app uses both filename and PDF content analysis
- Add custom patterns to `config.py` for your specific companies
- Check the logs for unclassified files

## Security Notes

- Never commit `credentials.json` or `token.json` to version control
- These files are already in `.gitignore`
- Keep your credentials secure and don't share them

## Support

For issues or questions:
1. Check the logs for error messages
2. Run with `--dry-run` to preview changes
3. Verify your Google Drive permissions
4. Check the GitHub repository for updates
