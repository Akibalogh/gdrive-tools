# Duplicate Handling Guide

## Overview

The Google Drive Statement Organizer now includes comprehensive duplicate detection and handling capabilities to prevent file duplication and provide intelligent file management.

## Types of Duplicates Detected

### 1. **Content Duplicates (MD5 Hash)**
- **What**: Files with identical content but potentially different names
- **Detection**: MD5 checksum comparison
- **Example**: `statement_jan.pdf` and `january_bill.pdf` with same content
- **Action**: Skip by default (prevents storage waste)

### 2. **Filename Duplicates**
- **What**: Files with identical names in the same destination folder
- **Detection**: Exact filename match in target folder
- **Example**: `statement.pdf` already exists in destination
- **Action**: Auto-rename with (1), (2), etc. or skip based on strategy

### 3. **Similar Filenames**
- **What**: Files with similar base names (different dates, extensions)
- **Detection**: Pattern matching on base names
- **Example**: `statement_2024-01.pdf` vs `statement_2024-01-15.pdf`
- **Action**: Inform user, allow manual decision

## Duplicate Handling Strategies

### **`--duplicate-handling smart` (Default)**
- **Behavior**: Automatically detects and handles duplicates intelligently
- **Content duplicates**: Skip (same MD5 hash)
- **Filename duplicates**: Auto-rename with incremental numbers
- **Similar filenames**: Inform user, proceed with copy
- **Best for**: Most use cases, provides intelligent automation

### **`--duplicate-handling skip`**
- **Behavior**: Skip all duplicate files regardless of type
- **Content duplicates**: Skip
- **Filename duplicates**: Skip
- **Similar filenames**: Skip
- **Best for**: Conservative approach, avoid any potential conflicts

### **`--duplicate-handling rename`**
- **Behavior**: Force rename all potential duplicates
- **Content duplicates**: Skip (still prevents waste)
- **Filename duplicates**: Auto-rename with (1), (2), etc.
- **Similar filenames**: Auto-rename to ensure uniqueness
- **Best for**: Ensuring all files are copied with unique names

### **`--duplicate-handling force`**
- **Behavior**: Force copy without duplicate checking
- **Content duplicates**: Copy (may create duplicates)
- **Filename duplicates**: Copy (may overwrite or create conflicts)
- **Similar filenames**: Copy without analysis
- **Best for**: When you want to override all duplicate detection

## Command Line Usage

### **Analyze Existing Duplicates**
```bash
# Scan destination folders for existing duplicates
python main.py --analyze-duplicates

# This provides a comprehensive report of:
# - Content duplicates (identical files)
# - Filename duplicates
# - Similar filename patterns
# - Recommendations for cleanup
```

### **Organize with Duplicate Handling**
```bash
# Use smart duplicate detection (default)
python main.py --duplicate-handling smart

# Skip all duplicates
python main.py --duplicate-handling skip

# Auto-rename all duplicates
python main.py --duplicate-handling rename

# Force copy without duplicate checking
python main.py --duplicate-handling force
```

### **Combined Operations**
```bash
# Analyze duplicates first, then organize with smart handling
python main.py --analyze-duplicates
python main.py --duplicate-handling smart

# Dry run to see how duplicates would be handled
python main.py --duplicate-handling smart --dry-run
```

## Technical Implementation

### **Duplicate Detection Process**
1. **File Metadata Retrieval**: Get file size, MD5 hash, and name
2. **Exact Match Check**: Look for identical filenames in destination
3. **Content Hash Check**: Compare MD5 checksums for content duplicates
4. **Similar Name Analysis**: Pattern matching on base names
5. **Action Recommendation**: Determine best course of action

### **Filename Generation**
- **Incremental Naming**: `filename.pdf` → `filename (1).pdf` → `filename (2).pdf`
- **Timestamp Fallback**: If 100+ duplicates, use timestamp: `filename_1234567890.pdf`
- **Uniqueness Guarantee**: Ensures no filename conflicts in destination

### **Performance Considerations**
- **API Calls**: Each duplicate check requires 1-2 API calls
- **Caching**: Results are cached to avoid repeated checks
- **Batch Processing**: Duplicate detection integrated with file organization pipeline

## Best Practices

### **For New Organizations**
1. **Start with Analysis**: Use `--analyze-duplicates` to understand current state
2. **Use Smart Handling**: Default `--duplicate-handling smart` for most cases
3. **Dry Run First**: Always test with `--dry-run` to see duplicate handling

### **For Existing Organized Folders**
1. **Regular Analysis**: Periodically run `--analyze-duplicates` to find new duplicates
2. **Cleanup Strategy**: Decide whether to keep, rename, or remove duplicates
3. **Consistent Naming**: Use consistent naming conventions to minimize future duplicates

### **For Large File Collections**
1. **Batch Processing**: Process files in smaller batches to manage memory
2. **Progress Monitoring**: Watch for duplicate detection progress in large operations
3. **Error Handling**: Duplicate detection errors won't stop the overall process

## Troubleshooting

### **Common Issues**

#### **"Could not check for duplicates" Warning**
- **Cause**: API error or file access issue
- **Solution**: File will be copied normally, check logs for details
- **Impact**: Minimal - only affects duplicate detection, not file copying

#### **High Duplicate Counts**
- **Cause**: Many similar files or repeated processing
- **Solution**: Use `--analyze-duplicates` to identify patterns
- **Prevention**: Review source folder organization

#### **Performance Issues**
- **Cause**: Large number of files requiring duplicate checks
- **Solution**: Use `--duplicate-handling skip` for faster processing
- **Alternative**: Process files in smaller batches

### **Debugging Duplicate Detection**
```bash
# Enable verbose logging
export PYTHONPATH=.
python -c "
from main import GoogleDriveOrganizer
org = GoogleDriveOrganizer()
# Test duplicate detection on specific file
result = org.check_for_duplicates('FILE_ID', 'FOLDER_ID')
print(result)
"
```

## Examples

### **Example 1: Smart Duplicate Handling**
```bash
python main.py --duplicate-handling smart

# Output:
# 🔄 Renaming duplicate: statement.pdf → statement (1).pdf
# ⏭️  Skipped: january_bill.pdf - Identical content already exists
# ✓ Copied: march_statement.pdf
```

### **Example 2: Duplicate Analysis Report**
```bash
python main.py --analyze-duplicates

# Output:
# Duplicate Analysis Results:
# Total files analyzed: 1,247
# MD5 duplicate groups: 3
# Filename duplicate groups: 12
# 
# Content Duplicates (Identical Files):
#   MD5: a1b2c3d4... - 2 files:
#     • statement_jan.pdf (Chase Freedom Card -64649/)
#     • january_bill.pdf (Chase Freedom Card -64649/)
```

### **Example 3: Skip All Duplicates**
```bash
python main.py --duplicate-handling skip

# Output:
# ⏭️  Skipped: statement.pdf - File with same name exists but content differs
# ⏭️  Skipped: january_bill.pdf - Identical content already exists
# ✓ Copied: march_statement.pdf
```

## Conclusion

The duplicate handling system provides intelligent, flexible, and efficient management of file duplicates during Google Drive organization. By understanding the different duplicate types and handling strategies, you can optimize your file organization workflow while preventing storage waste and maintaining data integrity.

For questions or issues with duplicate handling, refer to the main README.md or run `python main.py --help` for command-line options.
