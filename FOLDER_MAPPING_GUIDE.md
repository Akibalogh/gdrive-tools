# 📁 Google Drive Statement Organizer - Folder Mapping Guide

## 🎯 How Files Map to Your Existing Folders

Based on your existing 23 folders, here's exactly how different statement types will be organized:

---

## 🏦 **BANKING STATEMENTS**

### **Chase Bank Statements**
- **Filenames like:** `chase_bank_statement_*.pdf`, `jpmorgan_checking_*.pdf`
- **Maps to:** `Personal Checking -624` OR `Business Checking -417`
- **Logic:** Matches account number from filename/PDF content

### **Schwab Bank Statements** 
- **Filenames like:** `schwab_bank_statement_*.pdf`, `schwab_checking_*.pdf`
- **Maps to:** `Schwab Checking -7641`
- **Logic:** Direct company + account type match

### **SoFi Bank Statements**
- **Filenames like:** `sofi_bank_statement_*.pdf`, `sofi_money_*.pdf`
- **Maps to:** `SoFi Money`
- **Logic:** Company match + "money" product name

---

## 💳 **CREDIT CARD STATEMENTS**

### **American Express Cards**
- **Blue Business Plus:** `amex_blue_business_plus_*.pdf` → `Blue Business Plus Credit Card`
- **Blue Business Cash:** `amex_blue_business_cash_*.pdf` → `AmEx Blue Business Cash`  
- **Blue Cash Personal:** `amex_blue_cash_*.pdf` → `AmEx Blue Cash`
- **Business Express:** `schwab_amex_*.pdf` → `Schwab Business American Express`

### **Citi Cards**
- **American Airlines:** `citi_american_airlines_*5619.pdf` → `Citi American Airlines -5619`
- **Best Buy Card:** `citi_best_buy_*1383.pdf` → `Citi Best Buy -1383`
- **Double Cash:** `citi_double_cash_*.pdf` → `Citi Double Cash Personal`

### **Chase Cards**
- **Freedom Card:** `chase_freedom_*.pdf` → `Chase Freedom Card`
- **Other Chase Cards:** Will create new folders following pattern

### **Capital One Cards**
- **Quicksilver:** `capital_one_quicksilver_*.pdf` → `Capital One Quicksilver Credit Card`

### **Synchrony Cards**
- **Amazon Store Card:** `synchrony_amazon_*.pdf` → `Amazon Store Card - Synchrony`

---

## 📈 **INVESTMENT/BROKERAGE STATEMENTS**

### **Schwab Brokerage**
- **Personal Account:** `schwab_brokerage_*608.pdf` → `Personal Brokerage -608`
- **Business Account:** `schwab_brokerage_*485.pdf` → `Antifragile Broker -485`

### **IRA Accounts** (Currently marked as "Skip")
- **AltoIRA:** `alto_ira_*.pdf` → `IRA Accounts - Not reconciled anymore - Skip/AltoIRA`
- **Roth Manual:** `roth_ira_*625.pdf` → `IRA Accounts - Not reconciled anymore - Skip/Roth IRA Manual -625`
- **Roth Robo:** `roth_ira_*121.pdf` → `IRA Accounts - Not reconciled anymore - Skip/Roth IRA Robo -121`

---

## 🪙 **CRYPTO/TRADING STATEMENTS**

### **OkCoin**
- **Funding History:** `okcoin_funding_*.pdf` → `OkCoin/Funding Account History`
- **Spot Trading:** `okcoin_spot_*.pdf` → `OkCoin/Spot History`

### **Swan Bitcoin**
- **Swan/Prime Trust:** `swan_bitcoin_*.pdf` → `Swan Bitcoin / Prime Trust LLC`

---

## 💰 **LOAN STATEMENTS**

### **American Express Loans**
- **Personal Loan:** `amex_personal_loan_*.pdf` → `AmEx Personal Loan`

### **SoFi Loans**
- **SoFi Loan:** `sofi_loan_*.pdf` → `SoFi Loan`

---

## 🌐 **OTHER SERVICES**

### **PayPal**
- **Personal PayPal:** `paypal_*.pdf` → `Personal PayPal`

### **Wise (TransferWise)**
- **Wise Statements:** `wise_*.pdf` OR `transferwise_*.pdf` → `Wise`

---

## 🆕 **NEW FOLDER CREATION RULES**

When no existing folder matches, the app creates new folders following your naming pattern:

### **Format Examples:**
- **Credit Cards:** `[Company] [Product Name] -[Last4Digits]`
  - `Chase Sapphire Preferred -1234`
  - `Wells Fargo Active Cash -5678`

- **Bank Accounts:** `[Account Type] -[Last4Digits]`
  - `Wells Fargo Checking -9012`
  - `Bank of America Savings -3456`

- **Investment Accounts:** `[Company] [Account Type] -[Last4Digits]`
  - `Fidelity Brokerage -7890`
  - `Vanguard IRA -2345`

---

## 🔍 **MATCHING LOGIC**

The app uses this priority order:

1. **🎯 Exact Account Match:** File with account digits matches existing folder
2. **🏢 Company + Type Match:** Company and statement type match existing folder  
3. **📝 Keyword Match:** Product keywords match existing folder names
4. **➕ Create New:** No match found, create following your naming pattern

### **Account Number Extraction:**
- From filename: `*_account_1234.pdf` → `1234`
- From PDF content: "Account Number: 1234-5678" → `5678`
- Uses last 4 digits for folder naming

### **Company Keywords:**
- **American Express:** `amex`, `american express`, `blue`
- **Chase:** `chase`, `freedom`, `jpmorgan`
- **Citi:** `citi`, `best buy`, `american airlines`, `double cash`
- **Schwab:** `schwab`, `charles schwab`
- **Capital One:** `capital one`, `quicksilver`
- **Synchrony:** `synchrony`, `amazon store`
- **SoFi:** `sofi`

---

## 📊 **EXPECTED RESULTS**

From your **781 PDF files**, expect:

### **High Confidence Matches (90%+):**
- Files with account numbers in filename
- Clear company + product name combinations
- Standard statement naming patterns

### **Medium Confidence (70-90%):**
- Files requiring PDF content analysis
- Generic statement names needing context
- Multiple possible folder matches

### **Manual Review Needed (<70%):**
- Completely unrecognized companies
- Ambiguous statement types
- Files with corrupted/unreadable content

---

## 🚀 **Ready to Run!**

The system is designed to:
- ✅ **Preserve your existing organization**
- ✅ **Match your naming conventions**  
- ✅ **Handle multiple accounts per company**
- ✅ **Create new folders when needed**
- ✅ **Cache results for speed**

Use `--dry-run` first to see exactly where each file will go before making changes!
