import pandas as pd
files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 80)
print("BLUESTOCK MUTUAL FUND ANALYTICS - DATA INGESTION")
print("=" * 80)

for file in files:
    print("\n" + "=" * 80)
    print(f"DATASET: {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(f"data/raw/{file}")
        print("\n1. SHAPE")
        print(df.shape)
        print("\n2. DATA TYPES")
        print(df.dtypes)
        print("\n3. FIRST 5 ROWS")
        print(df.head())
        print("\n4. MISSING VALUES")
        print(df.isnull().sum())
        print("\n5. DUPLICATE ROWS")
        print(df.duplicated().sum())

        print("\nDataset loaded successfully!")

    except Exception as e:
        print(f"\nError loading {file}")
        print(e)

print("\n" + "=" * 80)
print("DATA INGESTION COMPLETED")
print("=" * 80)

