import pandas as pd
nav = pd.read_csv("data/raw/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(
    by=["amfi_code", "date"]
)
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]
nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV history cleaned successfully")
print(f"Rows: {len(nav)}")
# ==========================
# INVESTOR TRANSACTIONS CLEANING
# ==========================

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Fix date format
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

# Standardize transaction type
txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"].isin(valid_types)
]

# Validate amount > 0
txn = txn[
    txn["amount_inr"] > 0
]

# Validate KYC status
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

# Remove duplicates
txn = txn.drop_duplicates()

# Save cleaned file
txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nInvestor transactions cleaned successfully")
print(f"Rows: {len(txn)}")
# ==========================
# SCHEME PERFORMANCE CLEANING
# ==========================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Numeric columns to validate

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Flag anomalies in returns

anomalies = perf[
    (perf["return_1yr_pct"] > 100) |
    (perf["return_1yr_pct"] < -100)
]

anomalies.to_csv(
    "reports/performance_anomalies.csv",
    index=False
)

# Validate expense ratio range

perf = perf[
    perf["expense_ratio_pct"].between(0.1, 2.5)
]

# Remove duplicates

perf = perf.drop_duplicates()

# Save cleaned file

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nScheme performance cleaned successfully")
print(f"Rows: {len(perf)}")