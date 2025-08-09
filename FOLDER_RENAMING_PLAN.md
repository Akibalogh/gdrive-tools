# 📁 Google Drive Folder Renaming Plan

## 🎯 **CURRENT → NEW FOLDER NAMES**

### ✅ **CONFIRMED RENAMINGS (Ready to execute):**

#### 🏦 **Banking Accounts:**
1. `Personal Checking -624` → `Personal Checking -70624`
2. `Business Checking -417` → `Business Checking -71417`  
3. `Schwab Checking -7641` → `Schwab DLC Checking -17641` *(also correcting the name)*
4. `SoFi Money` → `SoFi Money -XXXXX` *(need 5 digits)*

#### 📈 **Investment/Brokerage:**
5. `Personal Brokerage -608` → `Personal Brokerage -05129`
6. `Antifragile Broker -485` → `Antifragile Broker -06412`
7. `Roth IRA Robo -121` → `Roth IRA Robo -XXXXX` *(need 5 digits)*
8. `Roth IRA Manual -625` → `Roth IRA Manual -XXXXX` *(need 5 digits)*

---

### ❓ **PENDING RENAMINGS (Need account numbers):**

#### 💳 **Credit Cards:**
9. `Citi American Airlines -5619` → `Citi American Airlines -XXXXX` *(expand to 5 digits)*
10. `Citi Best Buy -1383` → `Citi Best Buy -XXXXX` *(expand to 5 digits)*
11. `Citi Double Cash Personal` → `Citi Double Cash Personal -XXXXX`
12. `Chase Freedom Card` → `Chase Freedom Card -XXXXX` *(possibly -64548?)*
13. `Blue Business Plus Credit Card` → `Blue Business Plus Credit Card -XXXXX`
14. `AmEx Blue Business Cash` → `AmEx Blue Business Cash -XXXXX`
15. `AmEx Blue Cash` → `AmEx Blue Cash -XXXXX`
16. `Capital One Quicksilver Credit Card` → `Capital One Quicksilver Credit Card -XXXXX`
17. `Amazon Store Card - Synchrony` → `Amazon Store Card - Synchrony -XXXXX`
18. `Schwab Business American Express` → `Schwab Business American Express -XXXXX`

#### 💰 **Loans:**
19. `AmEx Personal Loan` → `AmEx Personal Loan -XXXXX`
20. `SoFi Loan` → `SoFi Loan -XXXXX`

#### 🪙 **Crypto/Trading:**
21. `Swan Bitcoin / Prime Trust LLC` → `Swan Bitcoin / Prime Trust LLC -XXXXX`
22. `AltoIRA` → `AltoIRA -XXXXX`

#### 🌐 **Services:**
23. `Personal PayPal` → `Personal PayPal -XXXXX` *(if applicable)*
24. `Wise` → `Wise -XXXXX` *(if applicable)*

---

## 🛠️ **RENAMING IMPLEMENTATION PLAN:**

### **Phase 1: Execute Confirmed Renamings (8 folders)**
```python
# Confirmed account numbers - ready to rename
confirmed_renames = {
    'Personal Checking -624': 'Personal Checking -70624',
    'Business Checking -417': 'Business Checking -71417', 
    'Schwab Checking -7641': 'Schwab DLC Checking -17641',
    'Personal Brokerage -608': 'Personal Brokerage -05129',
    'Antifragile Broker -485': 'Antifragile Broker -06412',
    'Roth IRA Robo -121': 'Roth IRA Robo -XXXXX',  # Need digits
    'Roth IRA Manual -625': 'Roth IRA Manual -XXXXX',  # Need digits
}
```

### **Phase 2: Get Missing Account Numbers**
- Extract remaining numbers from PDFs or 1Password
- Confirm which Chase card is "Freedom Card" (64548?)
- Get AmEx card numbers
- Get SoFi, Capital One, Synchrony numbers

### **Phase 3: Execute Remaining Renamings**
- Rename all credit cards with 5-digit endings
- Rename service accounts
- Update folder mapping logic to match new names

---

## 🎯 **GOOGLE DRIVE API RENAMING FUNCTIONS NEEDED:**

```python
def rename_folder(folder_id: str, new_name: str):
    """Rename a Google Drive folder"""
    # Will implement Google Drive API call to update folder name
    
def batch_rename_folders(rename_mapping: dict):
    """Batch rename multiple folders"""
    # Will iterate through confirmed renames
```

---

## ⚠️ **IMPORTANT CONSIDERATIONS:**

1. **Backup Strategy**: Export current folder structure before renaming
2. **File References**: Ensure no broken links after renaming  
3. **Batch Operations**: Rename in phases to avoid API limits
4. **Rollback Plan**: Keep mapping of old → new names for rollback
5. **Testing**: Start with 1-2 folders to test the process

---

## 📋 **CURRENT STATUS:**
- ✅ **8 confirmed renames** ready to execute
- ❓ **15+ pending renames** waiting for account numbers
- 🛠️ **Renaming functions** need to be implemented
- 🔄 **Folder mapping logic** needs updating after renames

**Ready to proceed with Phase 1 when you give the go-ahead!** 🚀
