## Progress

### Day 1 Completed
- Project setup and GitHub repository created
- Loaded and validated all 10 datasets
- Fetched live NAV data from mfapi.in
- Explored fund master metadata
- Completed AMFI code validation


## Day 2 – Data Cleaning & SQLite Integration

### Objective

Transform raw mutual fund datasets into analysis-ready data, design a star-schema database model, and load cleaned data into SQLite for analytical querying.

### Tasks Completed

#### Data Cleaning

Cleaned and validated the following datasets:

* `02_nav_history.csv`
* `07_scheme_performance.csv`
* `08_investor_transactions.csv`

Data quality checks performed:

* Converted date fields to proper datetime format
* Sorted NAV data by AMFI code and date
* Forward-filled missing NAV values where applicable
* Removed duplicate records
* Validated NAV values greater than zero
* Standardized transaction types (SIP, Lumpsum, Redemption)
* Validated transaction amounts
* Verified KYC status values
* Converted performance metrics to numeric format
* Flagged anomalous return values
* Validated expense ratio ranges

#### SQLite Database Design

Designed a star-schema data model consisting of:

**Dimension Tables**

* `dim_fund`
* `dim_date`

**Fact Tables**

* `fact_nav`
* `fact_transactions`
* `fact_performance`
* `fact_aum`

Database schema stored in:
sql/schema.sql
#### Database Loading

Used SQLAlchemy and Pandas to load cleaned datasets into SQLite.

Database created:
database/bluestock_mf.db


#### Analytical SQL Queries

Created analytical queries for:

* Top fund houses by AUM
* Average NAV analysis
* SIP transaction analysis
* State-wise transaction distribution
* Expense ratio screening
* Fund performance ranking
* KYC analysis
* AUM trend analysis

Stored in:
sql/queries.sql

#### Documentation

Created:
reports/data_dictionary.md
Documented:

* Column names
* Data types
* Business definitions
* Dataset references

### Deliverables
data/processed/
├── 02_nav_history_clean.csv
├── 07_scheme_performance_clean.csv
└── 08_investor_transactions_clean.csv

database/
└── bluestock_mf.db

sql/
├── schema.sql
└── queries.sql

reports/
├── data_dictionary.md
└── performance_anomalies.csv

### Technologies Used

* Python
* Pandas
* SQLite
* SQLAlchemy
* Git & GitHub


