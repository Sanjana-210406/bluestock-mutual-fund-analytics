# Data Dictionary

## 01_fund_master

| Column | Type | Description |
|----------|---------|-------------|
| amfi_code | Integer | Unique fund identifier |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Scheme name |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |

---

## 02_nav_history

| Column | Type | Description |
|----------|---------|-------------|
| amfi_code | Integer | Fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 03_aum_by_fund_house

| Column | Type | Description |
|----------|---------|-------------|
| date | Date | Reporting date |
| fund_house | Text | AMC name |
| aum_crore | Float | Assets Under Management |

---

## 07_scheme_performance

| Column | Type | Description |
|----------|---------|-------------|
| return_1yr_pct | Float | One-year return |
| return_3yr_pct | Float | Three-year return |
| return_5yr_pct | Float | Five-year return |
| expense_ratio_pct | Float | Expense ratio |

---

## 08_investor_transactions

| Column | Type | Description |
|----------|---------|-------------|
| investor_id | Text | Investor identifier |
| transaction_date | Date | Transaction date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction amount |
| kyc_status | Text | KYC verification status |

Source: Bluestock Mutual Fund Analytics Capstone datasets.