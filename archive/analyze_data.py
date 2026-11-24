import pandas as pd
import numpy as np
from datetime import datetime
import json

# Read the CSV file
df = pd.read_csv('lecture-file.csv')

# Basic information
print("=" * 80)
print("DATASET OVERVIEW")
print("=" * 80)
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"\nColumn names:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

print("\n" + "=" * 80)
print("DATA TYPES")
print("=" * 80)
print(df.dtypes)

print("\n" + "=" * 80)
print("MISSING VALUES ANALYSIS")
print("=" * 80)
missing_data = df.isnull().sum()
missing_percent = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'Column': missing_data.index,
    'Missing Count': missing_data.values,
    'Missing %': missing_percent.values
})
print(missing_df.to_string(index=False))

print("\n" + "=" * 80)
print("DUPLICATE COMPLAINT IDS")
print("=" * 80)
duplicates = df['complaint_id'].duplicated().sum()
print(f"Duplicate complaint IDs: {duplicates}")
print(f"Unique complaint IDs: {df['complaint_id'].nunique()}")

print("\n" + "=" * 80)
print("FINANCIAL PRODUCT ANALYSIS")
print("=" * 80)
print(f"Unique financial products: {df['financial_product'].nunique()}")
print("\nFinancial product distribution:")
product_counts = df['financial_product'].value_counts().sort_values(ascending=False)
for product, count in product_counts.items():
    print(f"  {product}: {count} ({count/len(df)*100:.2f}%)")

print("\n" + "=" * 80)
print("RESPONSE STATUS ANALYSIS")
print("=" * 80)
status_counts = df['response_status'].value_counts()
print(f"Total complaints: {len(df)}")
for status, count in status_counts.items():
    print(f"  {status}: {count} ({count/len(df)*100:.2f}%)")

print("\n" + "=" * 80)
print("TIMELY RESPONSE ANALYSIS")
print("=" * 80)
timely_counts = df['timely_response'].value_counts()
for response, count in timely_counts.items():
    print(f"  {response}: {count}")
    
# Calculate timely response rate for closed complaints only
closed_df = df[df['response_status'] == 'Closed'].copy()
closed_with_timely = closed_df[closed_df['timely_response'].notna()]
if len(closed_with_timely) > 0:
    timely_yes = (closed_with_timely['timely_response'] == 'Yes').sum()
    timely_no = (closed_with_timely['timely_response'] == 'No').sum()
    timely_rate = (timely_yes / (timely_yes + timely_no)) * 100 if (timely_yes + timely_no) > 0 else 0
    print(f"\nTimely Response Rate (Closed complaints only): {timely_rate:.2f}%")
    print(f"  Timely Yes: {timely_yes}")
    print(f"  Timely No: {timely_no}")

print("\n" + "=" * 80)
print("COMPANY ANALYSIS")
print("=" * 80)
print(f"Unique companies: {df['company_name'].nunique()}")
print("\nComplaints by company:")
company_counts = df['company_name'].value_counts().sort_values(ascending=False)
for company, count in company_counts.items():
    print(f"  {company}: {count}")

print("\n" + "=" * 80)
print("STATE ANALYSIS")
print("=" * 80)
print(f"Unique states: {df['state'].nunique()}")
state_missing = df['state'].isnull().sum()
print(f"Missing state values: {state_missing}")
print("\nTop 10 states by complaint volume:")
top_states = df['state'].value_counts().head(10)
for state, count in top_states.items():
    print(f"  {state}: {count}")

print("\n" + "=" * 80)
print("SUBMISSION CHANNEL ANALYSIS")
print("=" * 80)
channel_counts = df['submission_channel'].value_counts()
for channel, count in channel_counts.items():
    print(f"  {channel}: {count} ({count/len(df)*100:.2f}%)")

print("\n" + "=" * 80)
print("ISSUE CATEGORY ANALYSIS")
print("=" * 80)
print(f"Unique issue categories: {df['issue_category'].nunique()}")
print("\nTop 10 issue categories:")
top_issues = df['issue_category'].value_counts().head(10)
for issue, count in top_issues.items():
    print(f"  {issue}: {count}")

print("\n" + "=" * 80)
print("COMPANY RESPONSE ANALYSIS")
print("=" * 80)
response_counts = df['company_response'].value_counts()
for response, count in response_counts.items():
    print(f"  {response}: {count}")

print("\n" + "=" * 80)
print("DATE ANALYSIS")
print("=" * 80)
# Convert date columns
df['date_received'] = pd.to_datetime(df['date_received'], errors='coerce')
df['date_company_responded'] = pd.to_datetime(df['date_company_responded'], errors='coerce')
df['response_due_date'] = pd.to_datetime(df['response_due_date'], errors='coerce')

print(f"Date received range: {df['date_received'].min()} to {df['date_received'].max()}")
print(f"Date company responded range: {df['date_company_responded'].min()} to {df['date_company_responded'].max()}")

# Calculate average response time for closed complaints
closed_with_dates = df[
    (df['response_status'] == 'Closed') & 
    (df['date_received'].notna()) & 
    (df['date_company_responded'].notna())
].copy()

if len(closed_with_dates) > 0:
    closed_with_dates['response_time_days'] = (
        closed_with_dates['date_company_responded'] - closed_with_dates['date_received']
    ).dt.days
    
    avg_response_time = closed_with_dates['response_time_days'].mean()
    median_response_time = closed_with_dates['response_time_days'].median()
    min_response_time = closed_with_dates['response_time_days'].min()
    max_response_time = closed_with_dates['response_time_days'].max()
    
    print(f"\nResponse time analysis (Closed complaints only):")
    print(f"  Average: {avg_response_time:.2f} days")
    print(f"  Median: {median_response_time:.0f} days")
    print(f"  Min: {min_response_time} days")
    print(f"  Max: {max_response_time} days")
    print(f"  Total closed with valid dates: {len(closed_with_dates)}")

print("\n" + "=" * 80)
print("DATA QUALITY ISSUES")
print("=" * 80)

# Check for inconsistent financial product names (whitespace, casing)
print("Financial product variations (checking for formatting issues):")
unique_products = df['financial_product'].unique()
for product in sorted(unique_products):
    if product != product.strip():
        print(f"  WARNING: Product has leading/trailing spaces: '{product}'")
    if product != product.lower():
        print(f"  INFO: Product has mixed case: '{product}'")

# Check for open complaints with response dates
open_with_response = df[(df['response_status'] == 'Open') & (df['date_company_responded'].notna())]
print(f"\nOpen complaints with response dates: {len(open_with_response)} (potential data quality issue)")

# Check for closed complaints without response dates
closed_without_response = df[(df['response_status'] == 'Closed') & (df['date_company_responded'].isna())]
print(f"Closed complaints without response dates: {len(closed_without_response)} (data quality issue)")

# Check for open complaints with timely response flag
open_with_timely = df[(df['response_status'] == 'Open') & (df['timely_response'].notna())]
print(f"Open complaints with timely response flag: {len(open_with_timely)} (potential data quality issue)")

print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)
print(f"Dataset time period: {df['date_received'].min().strftime('%Y-%m-%d')} to {df['date_received'].max().strftime('%Y-%m-%d')}")
print(f"Total unique complaints: {df['complaint_id'].nunique()}")
print(f"Total duplicate records: {duplicates}")
print(f"Total financial products: {df['financial_product'].nunique()}")
print(f"Total companies: {df['company_name'].nunique()}")
print(f"Total states (excluding missing): {df['state'].nunique()}")
print(f"Open complaints: {(df['response_status'] == 'Open').sum()}")
print(f"Closed complaints: {(df['response_status'] == 'Closed').sum()}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
