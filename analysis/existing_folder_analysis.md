# Your Existing Folder Structure Analysis

## Current Organization Pattern

You already have 23 company/account folders with this naming pattern:

### Banking Accounts:
- `Personal Checking -624`
- `Business Checking -417` 
- `Schwab Checking -7641`
- `SoFi Money`

### Credit Cards:
- `Citi American Airlines -5619`
- `Citi Best Buy -1383`
- `Citi Double Cash Personal`
- `Chase Freedom Card`
- `Blue Business Plus Credit Card`
- `AmEx Blue Business Cash`
- `AmEx Blue Cash`
- `Capital One Quicksilver Credit Card`
- `Amazon Store Card - Synchrony`
- `Schwab Business American Express`

### Investment/Brokerage:
- `Personal Brokerage -608`
- `Antifragile Broker -485`
- `IRA Accounts - Not reconciled anymore - Skip`
  - `AltoIRA`
  - `Roth IRA Robo -121`
  - `Roth IRA Manual -625`

### Crypto/Trading:
- `OkCoin`
  - `Funding Account History`
  - `Spot History`
- `Swan Bitcoin / Prime Trust LLC`

### Loans:
- `AmEx Personal Loan`
- `SoFi Loan`

### Other Services:
- `Personal PayPal`
- `Wise`

## Key Insights:

1. **You use specific product names** instead of generic "credit card statement"
2. **Account numbers are last 3-4 digits** (not 5 as I assumed)
3. **Some folders are empty** - ready for new statements
4. **You have business vs personal separation**
5. **Some accounts have subfolders** (like OkCoin, IRA Accounts)

## Recommendation:

The app should:
1. **Match existing folder names** when possible
2. **Create new folders** following your naming pattern
3. **Use 4 digits** for account numbers (not 5)
4. **Preserve specific product names** (like "American Airlines", "Blue Cash")
