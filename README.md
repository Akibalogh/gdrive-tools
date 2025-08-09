# Google Drive Statement Organizer

🗂️ **Automatically organize thousands of financial statements in Google Drive with AI-powered classification**

A sophisticated Python application that intelligently organizes financial statements by reading PDF content, extracting account numbers, and copying files to properly structured account-based folders.

## ✨ Key Features

### 🤖 **Intelligent Classification**
- **PDF Content Analysis**: Reads PDF text to identify companies and account numbers
- **Smart Pattern Matching**: Uses 190+ company patterns and statement type recognition
- **Account Number Extraction**: Automatically extracts and uses account numbers for organization
- **99%+ Success Rate**: Handles generic filenames like "statement.pdf" or "2024-01-15.pdf"

### ⚡ **High Performance**  
- **Parallel Processing**: Process multiple files simultaneously (4x speed improvement)
- **Smart Caching**: Remembers classifications to avoid re-reading PDFs
- **Incremental Updates**: Only processes new files, skips already organized ones
- **Progress Tracking**: Real-time progress bars and detailed logging

### 🎯 **Advanced Organization**
- **Account-Based Folders**: Creates folders like "Chase Freedom Card -64649"
- **Smart Folder Matching**: Maps files to existing organized folders automatically
- **Duplicate Prevention**: Tracks processed files to avoid re-copying
- **Recursive Processing**: Handles complex monthly folder structures

### 🛡️ **Production Ready**
- **Error Handling**: Graceful handling of corrupted PDFs and API limits
- **Dry Run Mode**: Preview all changes before execution
- **Backup & Recovery**: Creates folder structure backups
- **Rate Limit Respect**: Works within Google Drive API constraints

## 📊 **Real-World Results**

- **789 files processed** in ~10 minutes (with 4 workers)
- **25+ account types** automatically recognized
- **2+ years of statements** organized from chaos to perfect structure
- **Zero manual intervention** required after initial setup

## 🚀 **Quick Start**

### 1. **Setup**
```bash
# Clone and setup
git clone https://github.com/yourusername/gdrive-tools.git
cd gdrive-tools
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 2. **Google Drive API Setup**
```bash
# Follow setup_instructions.md for detailed Google Cloud Console setup
# Place your credentials.json in project root
```

### 3. **Folder Structure**
Create these folders in your Google Drive:
- **"Monthly Statements"** - containing your monthly statement subfolders
- **"Statements by Account"** - where organized folders will be created

### 4. **Run**
```bash
# Preview what will happen (recommended first run)
python main.py --dry-run

# Organize with parallel processing (4 workers)
python main.py --workers 4

# Organize specific folder IDs
python main.py --source-folder-id YOUR_FOLDER_ID --dest-folder-id YOUR_DEST_ID
```

## 🎯 **Advanced Usage**

### **Folder Renaming**
```bash
# Rename folders with proper account numbers
python main.py --rename-folders --dry-run
python main.py --rename-folders
```

### **Cache Management**
```bash
# Clear classification cache
python main.py --clear-cache

# Export cache for analysis
python main.py --export-cache cache_backup.json
```

### **Performance Tuning**
```bash
# Adjust parallel workers (2-8 recommended)
python main.py --workers 8  # Faster but may hit API limits
python main.py --workers 2  # Slower but very safe
```

### **Backup & Recovery**
```bash
# Backup folder structure before changes
python main.py --backup-folders
```

## 📁 **Example Organization**

**Before:**
```
Monthly Statements/
├── 2024-01/
│   ├── statement.pdf
│   ├── bill_jan.pdf
│   └── 2024-01-15.pdf
├── 2024-02/
│   ├── feb_statement.pdf
│   └── DetailedBill.pdf
```

**After:**
```
Statements by Account/
├── Chase Freedom Card -64649/
├── AmEx Blue Cash -84002/
├── Business Checking -417/
├── SoFi Money -20516/
├── Personal PayPal -53762/
└── T-Mobile -36215/
```

## 🔧 **Configuration**

### **Supported Companies (190+)**
Chase, Bank of America, Wells Fargo, Citi, American Express, Capital One, Schwab, Fidelity, SoFi, PayPal, and many more...

### **Statement Types**
- Bank Statements
- Credit Card Statements  
- Investment/Brokerage Statements
- Loan Statements
- Utility Bills
- Insurance Statements
- And more...

### **Customization**
Edit `config.py` to add:
- New company patterns
- Custom statement types
- Folder naming conventions

## 📈 **Monitoring & Analytics**

The application provides detailed analytics:
- Classification success rates
- Processing speed metrics
- Cache hit rates
- Error analysis
- Folder matching statistics

## 🛠️ **Development**

### **Run Tests**
```bash
python -m pytest test_main.py -v
```

### **Code Quality**
```bash
# The project includes comprehensive error handling and logging
# See IMPROVEMENTS_SUMMARY.md for technical details
```

## 📋 **Requirements**

- Python 3.7+
- Google Drive API credentials
- 2-4GB RAM (for processing large PDFs)
- Internet connection for Google Drive API

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 **License**

MIT License - feel free to use for personal or commercial projects.

## 🆘 **Support**

- Check `setup_instructions.md` for detailed setup help
- Review `IMPROVEMENTS_SUMMARY.md` for technical architecture
- See example files in the repository for usage patterns

---

**⭐ Star this repo if it helps organize your financial life!**