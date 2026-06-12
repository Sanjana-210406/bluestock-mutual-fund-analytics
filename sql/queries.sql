-- 1. Top 5 fund houses by AUM

SELECT
fund_house,
MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV by fund

SELECT
amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Monthly average NAV

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 4. SIP transaction volume

SELECT
COUNT(*) AS sip_transactions
FROM fact_transactions
WHERE transaction_type='Sip';

-- 5. Transactions by state

SELECT
state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 6. Funds with expense ratio below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7. Top funds by 1-year return

SELECT
scheme_name,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 8. Average expense ratio

SELECT
AVG(expense_ratio_pct)
AS avg_expense_ratio
FROM fact_performance;

-- 9. Transactions by KYC status

SELECT
kyc_status,
COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Average AUM by fund house

SELECT
fund_house,
AVG(aum_crore) AS avg_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY avg_aum DESC;