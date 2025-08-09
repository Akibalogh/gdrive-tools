# Statement Organization Plan

Based on the dry run, here's how your statements will be organized:

## Folder Structure

```
Statements by Account/
├── american express/
│   ├── credit card - 12345/
│   ├── credit card - 67890/
│   ├── credit card - 54321/
│   └── credit card - 09876/  (if you have more cards)
├── chase/
│   ├── bank - 12345/          (Checking Account)
│   ├── bank - 67890/          (Savings Account)
│   ├── credit card - 54321/
│   ├── credit card - 09876/
│   └── investment - 11111/    (Brokerage Account)
├── citi/
│   ├── credit card - 12345/
│   ├── credit card - 67890/
│   └── credit card - 54321/
├── schwab/
│   ├── bank - 12345/          (Checking Account 1)
│   ├── bank - 67890/          (Checking Account 2)
│   ├── investment - 54321/    (Brokerage Account 1)
│   └── investment - 09876/    (Brokerage Account 2)
├── wells fargo/
│   ├── bank - 12345/
│   └── credit card - 67890/
└── td bank/
    └── bank - 54321/
```

## Account Detection

The app will automatically detect account information from:

### Filenames containing:
- `account_1234-5678`
- `ending_1234`
- `last_1234` 
- `#1234-5678`
- `checking_1234`
- `savings_1234`
- `brokerage_1234`

### PDF Content containing:
- "Account: 1234-5678"
- "Ending in 1234"
- "Last 4 digits: 1234"
- Credit card numbers (masked)

## Specific Examples from Your Files:

### American Express Cards
- **Multiple Amex cards** will be separated by last 5 digits
- Folders like: `credit card - 12345`, `credit card - 67890`

### Chase Accounts
- **Multiple Chase accounts** detected (checking, savings, credit cards)
- Will create separate folders like: `bank - 12345`, `credit card - 67890`

### Schwab Accounts
- **2 Checking accounts** → `bank - 12345`, `bank - 67890`
- **2 Brokerage accounts** → `investment - 54321`, `investment - 09876`

### Citi Cards
- **2-3 Credit cards** → `credit card - 12345`, `credit card - 67890`, `credit card - 54321`

## Files That Need Manual Review:

Some files couldn't be automatically classified and may need manual sorting:
- `DetailedBill.pdf` - Generic name, needs content analysis
- `090924 WellsFargo.pdf` - Wells Fargo detected but statement type unclear
- `Sept 2024.pdf` - Generic date name, no company detected

## Statistics from Your Drive:
- **789 total files** found
- **781 PDF files** (will be processed)
- **8 other files** (4 PNG, 1 ZIP, 3 CSV - will be skipped)

## Next Steps:
1. **Run actual organization**: `python main.py` (remove --dry-run)
2. **Review unclassified files**: Check the files that couldn't be classified
3. **Verify account separation**: Ensure multiple accounts are properly separated
4. **Add custom patterns**: If needed, we can add more specific patterns for your files

Would you like me to run the actual organization, or would you like to modify any of the classification patterns first?
