import pandas as pd
import numpy as np
from datetime import datetime
import json

# Read the original CSV file
df = pd.read_csv('lecture-file.csv')

print("=" * 80)
print("DATA RECONCILIATION AUDIT")
print("=" * 80)
print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# ===================================================================
# STEP 1: ANALYZE ORIGINAL DATA
# ===================================================================
print("=" * 80)
print("STEP 1: ORIGINAL DATA ANALYSIS")
print("=" * 80)

original_total = len(df)
original_unique = df['complaint_id'].nunique()
original_duplicates = original_total - original_unique

print(f"Total records in original CSV: {original_total}")
print(f"Unique complaint IDs: {original_unique}")
print(f"Duplicate records: {original_duplicates}")

# Status breakdown (original)
original_open = (df['response_status'] == 'Open').sum()
original_closed = (df['response_status'] == 'Closed').sum()

print(f"\nOriginal Status Breakdown:")
print(f"  Open: {original_open} ({original_open/original_total*100:.2f}%)")
print(f"  Closed: {original_closed} ({original_closed/original_total*100:.2f}%)")
print(f"  Total: {original_open + original_closed}")

# ===================================================================
# STEP 2: APPLY CLEANING RULES
# ===================================================================
print("\n" + "=" * 80)
print("STEP 2: APPLYING CLEANING RULES")
print("=" * 80)

# Cleaning Rule 1: Remove duplicates (keep='first')
print("\n[Rule 1] Duplicate Removal:")
duplicates_df = df[df['complaint_id'].duplicated(keep=False)].sort_values('complaint_id')
print(f"  Duplicate complaint IDs found: {original_duplicates}")
if original_duplicates > 0:
    print(f"  Sample duplicates:")
    for complaint_id in duplicates_df['complaint_id'].unique()[:5]:
        dupe_records = duplicates_df[duplicates_df['complaint_id'] == complaint_id]
        print(f"    {complaint_id}: {len(dupe_records)} occurrences")

# Apply duplicate removal
df_clean = df.drop_duplicates(subset=['complaint_id'], keep='first').copy()
print(f"  Strategy: Keep first occurrence")
print(f"  Records removed: {len(df) - len(df_clean)}")
print(f"  Records after cleaning: {len(df_clean)}")

# Cleaning Rule 2: Financial Product Standardization
print("\n[Rule 2] Financial Product Standardization:")
whitespace_products = df_clean[df_clean['financial_product'] != df_clean['financial_product'].str.strip()]
print(f"  Records with whitespace in financial_product: {len(whitespace_products)}")

df_clean['financial_product'] = df_clean['financial_product'].str.strip()
product_mapping = {
    'credit card': 'Credit card',
    'checking or savings account': 'Checking or savings account',
    'personal loan': 'Personal loan',
    'mortgage': 'Mortgage',
    'credit reporting': 'Credit reporting',
    'buy now, pay later': 'Buy now, pay later'
}
df_clean['financial_product'] = df_clean['financial_product'].str.lower().map(product_mapping)
print(f"  Products standardized to title case")

# Cleaning Rule 3: Submission Channel Standardization
print("\n[Rule 3] Submission Channel Standardization:")
whitespace_channels = df[df['submission_channel'] != df['submission_channel'].str.strip()]
print(f"  Records with whitespace in submission_channel: {len(whitespace_channels)}")

df_clean['submission_channel'] = df_clean['submission_channel'].str.strip()
channel_mapping = {
    'web': 'Web',
    'phone': 'Phone',
    'mail': 'Mail',
    'referral': 'Referral'
}
df_clean['submission_channel'] = df_clean['submission_channel'].str.lower().map(channel_mapping)
print(f"  Channels standardized to title case")

# Convert dates
df_clean['date_received'] = pd.to_datetime(df_clean['date_received'], errors='coerce')
df_clean['date_company_responded'] = pd.to_datetime(df_clean['date_company_responded'], errors='coerce')
df_clean['response_due_date'] = pd.to_datetime(df_clean['response_due_date'], errors='coerce')

# ===================================================================
# STEP 3: CALCULATE CORRECTED KPIs
# ===================================================================
print("\n" + "=" * 80)
print("STEP 3: CORRECTED KPI CALCULATIONS")
print("=" * 80)

# KPI 1: Total Complaints
total_complaints_cleaned = df_clean['complaint_id'].nunique()
print(f"\n1. Total Complaints (Unique):")
print(f"   Original: {original_total} records")
print(f"   Cleaned: {total_complaints_cleaned} unique complaints")
print(f"   Formula: DISTINCTCOUNT(complaint_id)")

# KPI 2 & 3: Open and Closed Complaints
open_complaints_cleaned = (df_clean['response_status'] == 'Open').sum()
closed_complaints_cleaned = (df_clean['response_status'] == 'Closed').sum()

print(f"\n2. Open Complaints:")
print(f"   Original: {original_open}")
print(f"   Cleaned: {open_complaints_cleaned}")
print(f"   Percentage: {open_complaints_cleaned/total_complaints_cleaned*100:.2f}%")

print(f"\n3. Closed Complaints:")
print(f"   Original: {original_closed}")
print(f"   Cleaned: {closed_complaints_cleaned}")
print(f"   Percentage: {closed_complaints_cleaned/total_complaints_cleaned*100:.2f}%")

print(f"\n   Verification: Open + Closed = Total?")
print(f"   {open_complaints_cleaned} + {closed_complaints_cleaned} = {open_complaints_cleaned + closed_complaints_cleaned}")
print(f"   Expected: {total_complaints_cleaned}")
print(f"   Match: {open_complaints_cleaned + closed_complaints_cleaned == total_complaints_cleaned}")

# KPI 4: Timely Response Rate
closed_df = df_clean[df_clean['response_status'] == 'Closed'].copy()
timely_yes = (closed_df['timely_response'] == 'Yes').sum()
timely_no = (closed_df['timely_response'] == 'No').sum()
timely_total = timely_yes + timely_no
timely_rate = (timely_yes / timely_total * 100) if timely_total > 0 else 0

print(f"\n4. Timely Response Rate:")
print(f"   Closed complaints: {closed_complaints_cleaned}")
print(f"   Closed with 'Yes': {timely_yes}")
print(f"   Closed with 'No': {timely_no}")
print(f"   Closed with timely data: {timely_total}")
print(f"   Timely Response Rate: {timely_rate:.2f}%")
print(f"   Formula: (Timely Yes / (Timely Yes + Timely No)) × 100")
print(f"   Note: Excludes Open complaints and Closed without timely flag")

# KPI 5: Average Response Time
closed_with_dates = df_clean[
    (df_clean['response_status'] == 'Closed') & 
    (df_clean['date_received'].notna()) & 
    (df_clean['date_company_responded'].notna())
].copy()

closed_with_dates['response_time_days'] = (
    closed_with_dates['date_company_responded'] - closed_with_dates['date_received']
).dt.days

avg_response_time = closed_with_dates['response_time_days'].mean()
median_response_time = closed_with_dates['response_time_days'].median()
min_response_time = closed_with_dates['response_time_days'].min()
max_response_time = closed_with_dates['response_time_days'].max()

print(f"\n5. Average Response Time:")
print(f"   Closed complaints with valid dates: {len(closed_with_dates)}")
print(f"   Average: {avg_response_time:.2f} days")
print(f"   Median: {median_response_time:.0f} days")
print(f"   Range: {min_response_time} to {max_response_time} days")
print(f"   Formula: AVG(date_company_responded - date_received)")
print(f"   Note: Only Closed complaints with both dates populated")

# ===================================================================
# STEP 4: RECALCULATE DISTRIBUTIONS
# ===================================================================
print("\n" + "=" * 80)
print("STEP 4: RECALCULATED DISTRIBUTIONS (CLEANED DATA)")
print("=" * 80)

# Financial Products
print("\n[A] Financial Product Distribution (After Cleaning):")
product_counts = df_clean['financial_product'].value_counts().sort_values(ascending=False)
for product, count in product_counts.items():
    pct = count/len(df_clean)*100
    print(f"  {product}: {count} ({pct:.2f}%)")

# Issue Categories
print("\n[B] Top 10 Issue Categories (After Cleaning):")
issue_counts = df_clean['issue_category'].value_counts().head(10)
for i, (issue, count) in enumerate(issue_counts.items(), 1):
    print(f"  {i}. {issue}: {count}")

# Companies
print("\n[C] Company Distribution (After Cleaning):")
company_counts = df_clean['company_name'].value_counts().sort_values(ascending=False)
for company, count in company_counts.items():
    pct = count/len(df_clean)*100
    print(f"  {company}: {count} ({pct:.2f}%)")

# Company-wise Timely Response Rate
print("\n[D] Company-wise Timely Response Rate (After Cleaning):")
company_timely = []
for company in df_clean['company_name'].unique():
    company_closed = df_clean[
        (df_clean['company_name'] == company) & 
        (df_clean['response_status'] == 'Closed')
    ]
    
    yes_count = (company_closed['timely_response'] == 'Yes').sum()
    no_count = (company_closed['timely_response'] == 'No').sum()
    total_with_flag = yes_count + no_count
    
    if total_with_flag > 0:
        rate = (yes_count / total_with_flag) * 100
        company_timely.append({
            'company': company,
            'total_complaints': len(df_clean[df_clean['company_name'] == company]),
            'closed': len(company_closed),
            'timely_yes': yes_count,
            'timely_no': no_count,
            'rate': rate
        })

company_timely_df = pd.DataFrame(company_timely).sort_values('rate', ascending=False)
for _, row in company_timely_df.iterrows():
    print(f"  {row['company']}: {row['rate']:.2f}% ({row['total_complaints']} total, {row['closed']} closed)")

# ===================================================================
# STEP 5: IDENTIFY CONTRADICTIONS
# ===================================================================
print("\n" + "=" * 80)
print("STEP 5: CONTRADICTIONS AND ISSUES IDENTIFIED")
print("=" * 80)

issues = []

# Issue 1: Real-time refresh vs static CSV
issues.append({
    "issue": "Real-time refresh claim contradicts static CSV architecture",
    "severity": "High",
    "location": "PRD Section 5.2.1 KPI Specifications",
    "correction": "Change 'Refresh: Real-time with data updates' to 'Refresh: Manual data reload required'"
})

# Issue 2: Using original counts in examples
issues.append({
    "issue": "Examples use original record counts instead of cleaned counts",
    "severity": "High",
    "location": "PRD Section 5.3.2, 5.3.3, 5.3.4",
    "correction": "Update all expected distributions to use cleaned dataset values"
})

# Issue 3: Timely response calculation not explicit about denominator
issues.append({
    "issue": "Timely Response Rate baseline shows 90.10% (4,225 Yes / 4,689 Closed) but should be 4,225/(4,225+464)",
    "severity": "Medium",
    "location": "PRD Section 5.2.1 KPI 4",
    "correction": "Clarify: 90.10% = 4,225 Yes / (4,225 Yes + 464 No), excluding Closed without timely flag"
})

# Issue 4: No deterministic duplicate removal rule
issues.append({
    "issue": "Duplicate removal rule not deterministic (no tie-breaker specified)",
    "severity": "Medium",
    "location": "TRD Section 4.3 Rule 1",
    "correction": "Specify: Keep first occurrence by row order in CSV (keep='first')"
})

# Issue 5: Company size disclaimer missing in charts
issues.append({
    "issue": "Company comparison charts don't prominently show that company sizes differ",
    "severity": "Low",
    "location": "PRD Section 5.3.4",
    "correction": "Add disclaimer to chart acceptance criteria"
})

for i, issue in enumerate(issues, 1):
    print(f"\n[Issue {i}] {issue['issue']}")
    print(f"  Severity: {issue['severity']}")
    print(f"  Location: {issue['location']}")
    print(f"  Correction: {issue['correction']}")

# ===================================================================
# STEP 6: GENERATE RECONCILIATION SUMMARY
# ===================================================================
print("\n" + "=" * 80)
print("STEP 6: RECONCILIATION SUMMARY")
print("=" * 80)

reconciliation = {
    "audit_date": datetime.now().isoformat(),
    "source_file": "lecture-file.csv",
    "original_data": {
        "total_records": int(original_total),
        "unique_complaints": int(original_unique),
        "duplicate_records": int(original_duplicates),
        "open_complaints": int(original_open),
        "closed_complaints": int(original_closed)
    },
    "cleaned_data": {
        "total_records": int(len(df_clean)),
        "unique_complaints": int(total_complaints_cleaned),
        "duplicate_records_removed": int(original_duplicates),
        "open_complaints": int(open_complaints_cleaned),
        "closed_complaints": int(closed_complaints_cleaned)
    },
    "kpi_baselines": {
        "total_complaints": int(total_complaints_cleaned),
        "open_complaints": {
            "count": int(open_complaints_cleaned),
            "percentage": float(f"{open_complaints_cleaned/total_complaints_cleaned*100:.2f}")
        },
        "closed_complaints": {
            "count": int(closed_complaints_cleaned),
            "percentage": float(f"{closed_complaints_cleaned/total_complaints_cleaned*100:.2f}")
        },
        "timely_response_rate": {
            "percentage": float(f"{timely_rate:.2f}"),
            "timely_yes": int(timely_yes),
            "timely_no": int(timely_no),
            "total_with_flag": int(timely_total)
        },
        "average_response_time": {
            "days": float(f"{avg_response_time:.2f}"),
            "median_days": float(median_response_time),
            "min_days": int(min_response_time),
            "max_days": int(max_response_time),
            "sample_size": int(len(closed_with_dates))
        }
    },
    "verification": {
        "open_plus_closed_equals_total": bool(open_complaints_cleaned + closed_complaints_cleaned == total_complaints_cleaned),
        "data_quality_issues_found": len(issues)
    },
    "issues_identified": issues
}

print("\nReconciliation Summary:")
print(json.dumps(reconciliation, indent=2))

# Save reconciliation report
with open('reconciliation_report.json', 'w') as f:
    json.dump(reconciliation, f, indent=2)

print("\n✓ Reconciliation report saved to: reconciliation_report.json")

# Save cleaned dataset
df_clean.to_csv('data/processed/complaints_cleaned.csv', index=False)
print("✓ Cleaned dataset saved to: data/processed/complaints_cleaned.csv")

print("\n" + "=" * 80)
print("AUDIT COMPLETE")
print("=" * 80)
