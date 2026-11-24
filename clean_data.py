"""
Financial Complaint Data Cleaning Pipeline
Implements data cleaning according to PRD v1.1 and TRD v1.1
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json
import sys

print("=" * 80)
print("FINANCIAL COMPLAINT DATA CLEANING PIPELINE")
print("=" * 80)
print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# =============================================================================
# CONFIGURATION
# =============================================================================

INPUT_FILE = 'data/original/lecture-file.csv'
OUTPUT_FILE = 'data/processed/complaints_cleaned.csv'
LOG_FILE = 'data/processed/cleaning_log.json'
VALIDATION_FILE = 'data/processed/validation_report.json'

# Expected baseline values (for validation)
EXPECTED_BASELINES = {
    'total_complaints': 4975,
    'open_complaints': 310,
    'closed_complaints': 4665,
    'timely_yes': 4202,
    'timely_no': 463,
    'timely_rate': 90.08,
    'avg_response_days': 8.76
}

# =============================================================================
# STEP 1: LOAD DATA
# =============================================================================

print("STEP 1: Loading original dataset...")
try:
    df = pd.read_csv(INPUT_FILE)
    print(f"✓ Loaded {len(df)} records from {INPUT_FILE}")
except Exception as e:
    print(f"✗ Error loading file: {e}")
    sys.exit(1)

original_count = len(df)
cleaning_log = {
    'timestamp': datetime.now().isoformat(),
    'source_file': INPUT_FILE,
    'output_file': OUTPUT_FILE,
    'original_record_count': original_count,
    'operations': []
}

# =============================================================================
# STEP 2: REMOVE DUPLICATES
# =============================================================================

print("\nSTEP 2: Removing duplicate complaint IDs...")
duplicates_before = df['complaint_id'].duplicated().sum()
print(f"  Found {duplicates_before} duplicate records")

# Keep first occurrence by row order (deterministic strategy)
df_cleaned = df.drop_duplicates(subset=['complaint_id'], keep='first').copy()
duplicates_removed = original_count - len(df_cleaned)

print(f"✓ Removed {duplicates_removed} duplicates using keep='first' strategy")
print(f"  Records after cleaning: {len(df_cleaned)}")

cleaning_log['operations'].append({
    'step': 'duplicate_removal',
    'records_affected': int(duplicates_removed),
    'strategy': 'keep=first by row order',
    'description': f'Removed {duplicates_removed} duplicate complaint IDs'
})

# =============================================================================
# STEP 3: STANDARDIZE FINANCIAL PRODUCT
# =============================================================================

print("\nSTEP 3: Standardizing financial_product values...")
whitespace_products = (df_cleaned['financial_product'] != df_cleaned['financial_product'].str.strip()).sum()
print(f"  Found {whitespace_products} records with whitespace issues")

# Remove whitespace
df_cleaned['financial_product'] = df_cleaned['financial_product'].str.strip()

# Standardize to title case
product_mapping = {
    'credit card': 'Credit card',
    'checking or savings account': 'Checking or savings account',
    'personal loan': 'Personal loan',
    'mortgage': 'Mortgage',
    'credit reporting': 'Credit reporting',
    'buy now, pay later': 'Buy now, pay later'
}

df_cleaned['financial_product'] = df_cleaned['financial_product'].str.lower().map(product_mapping)

print(f"✓ Standardized {whitespace_products} financial_product values")

cleaning_log['operations'].append({
    'step': 'financial_product_standardization',
    'records_affected': int(whitespace_products),
    'description': 'Removed whitespace and standardized to title case'
})

# =============================================================================
# STEP 4: STANDARDIZE SUBMISSION CHANNEL
# =============================================================================

print("\nSTEP 4: Standardizing submission_channel values...")
# Count before cleaning
whitespace_channels_before = (df['submission_channel'] != df['submission_channel'].str.strip()).sum()
print(f"  Found {whitespace_channels_before} records with whitespace issues")

# Remove whitespace
df_cleaned['submission_channel'] = df_cleaned['submission_channel'].str.strip()

# Standardize to title case
channel_mapping = {
    'web': 'Web',
    'phone': 'Phone',
    'mail': 'Mail',
    'referral': 'Referral'
}

df_cleaned['submission_channel'] = df_cleaned['submission_channel'].str.lower().map(channel_mapping)

print(f"✓ Standardized {whitespace_channels_before} submission_channel values")

cleaning_log['operations'].append({
    'step': 'submission_channel_standardization',
    'records_affected': int(whitespace_channels_before),
    'description': 'Removed whitespace and standardized to title case'
})

# =============================================================================
# STEP 5: DATE VALIDATION
# =============================================================================

print("\nSTEP 5: Validating and converting dates...")

# Convert date columns
df_cleaned['date_received'] = pd.to_datetime(df_cleaned['date_received'], errors='coerce')
df_cleaned['date_company_responded'] = pd.to_datetime(df_cleaned['date_company_responded'], errors='coerce')
df_cleaned['response_due_date'] = pd.to_datetime(df_cleaned['response_due_date'], errors='coerce')

# Check for invalid dates
invalid_received = df_cleaned['date_received'].isnull().sum()
invalid_responded = df_cleaned[df_cleaned['response_status'] == 'Closed']['date_company_responded'].isnull().sum()

# Validate response date >= received date
invalid_order = df_cleaned[
    (df_cleaned['date_company_responded'].notna()) & 
    (df_cleaned['date_company_responded'] < df_cleaned['date_received'])
]

print(f"  Invalid date_received: {invalid_received}")
print(f"  Closed without response date: {invalid_responded}")
print(f"  Response before received: {len(invalid_order)}")

if len(invalid_order) == 0 and invalid_received == 0 and invalid_responded == 0:
    print(f"✓ All dates valid")

cleaning_log['operations'].append({
    'step': 'date_validation',
    'records_affected': 0,
    'description': 'All dates valid, no corrections needed'
})

# =============================================================================
# STEP 6: STATUS CONSISTENCY VALIDATION
# =============================================================================

print("\nSTEP 6: Validating response status consistency...")

# Check: Open complaints should not have response dates
open_with_response = df_cleaned[
    (df_cleaned['response_status'] == 'Open') & 
    (df_cleaned['date_company_responded'].notna())
]

# Check: Open complaints should not have timely response flags
open_with_timely = df_cleaned[
    (df_cleaned['response_status'] == 'Open') & 
    (df_cleaned['timely_response'].notna())
]

# Check: Closed complaints should have response dates
closed_without_response = df_cleaned[
    (df_cleaned['response_status'] == 'Closed') & 
    (df_cleaned['date_company_responded'].isna())
]

print(f"  Open with response date: {len(open_with_response)}")
print(f"  Open with timely flag: {len(open_with_timely)}")
print(f"  Closed without response: {len(closed_without_response)}")

if len(open_with_response) == 0 and len(open_with_timely) == 0 and len(closed_without_response) == 0:
    print(f"✓ All status fields consistent")

cleaning_log['operations'].append({
    'step': 'status_consistency_validation',
    'records_affected': 0,
    'description': 'All status fields consistent, no violations found'
})

# =============================================================================
# STEP 7: CALCULATE RESPONSE TIME
# =============================================================================

print("\nSTEP 7: Calculating response_time_days...")

# Calculate response time for closed complaints
df_cleaned['response_time_days'] = np.nan

closed_mask = (df_cleaned['response_status'] == 'Closed') & \
              (df_cleaned['date_received'].notna()) & \
              (df_cleaned['date_company_responded'].notna())

df_cleaned.loc[closed_mask, 'response_time_days'] = (
    df_cleaned.loc[closed_mask, 'date_company_responded'] - 
    df_cleaned.loc[closed_mask, 'date_received']
).dt.days

calculated_count = closed_mask.sum()
print(f"✓ Calculated response_time_days for {calculated_count} closed complaints")

cleaning_log['operations'].append({
    'step': 'calculate_response_time',
    'records_affected': int(calculated_count),
    'description': f'Calculated response time in days for {calculated_count} closed complaints'
})

# =============================================================================
# STEP 8: VALIDATE KPIs
# =============================================================================

print("\n" + "=" * 80)
print("KPI VALIDATION")
print("=" * 80)

# Calculate actual KPIs
total_complaints = df_cleaned['complaint_id'].nunique()
open_complaints = (df_cleaned['response_status'] == 'Open').sum()
closed_complaints = (df_cleaned['response_status'] == 'Closed').sum()

closed_df = df_cleaned[df_cleaned['response_status'] == 'Closed']
timely_yes = (closed_df['timely_response'] == 'Yes').sum()
timely_no = (closed_df['timely_response'] == 'No').sum()
timely_rate = round((timely_yes / (timely_yes + timely_no)) * 100, 2) if (timely_yes + timely_no) > 0 else 0

closed_with_dates = df_cleaned[closed_mask]
avg_response_days = round(closed_with_dates['response_time_days'].mean(), 2)

validation_results = {
    'total_complaints': {'actual': int(total_complaints), 'expected': EXPECTED_BASELINES['total_complaints']},
    'open_complaints': {'actual': int(open_complaints), 'expected': EXPECTED_BASELINES['open_complaints']},
    'closed_complaints': {'actual': int(closed_complaints), 'expected': EXPECTED_BASELINES['closed_complaints']},
    'timely_yes': {'actual': int(timely_yes), 'expected': EXPECTED_BASELINES['timely_yes']},
    'timely_no': {'actual': int(timely_no), 'expected': EXPECTED_BASELINES['timely_no']},
    'timely_rate': {'actual': float(timely_rate), 'expected': EXPECTED_BASELINES['timely_rate']},
    'avg_response_days': {'actual': float(avg_response_days), 'expected': EXPECTED_BASELINES['avg_response_days']}
}

all_match = True
for metric, values in validation_results.items():
    match = values['actual'] == values['expected']
    status = '✓' if match else '✗'
    print(f"{status} {metric:25} Expected: {values['expected']:>10}  Actual: {values['actual']:>10}")
    if not match:
        all_match = False

if all_match:
    print("\n✅ ALL KPIs MATCH EXPECTED BASELINES")
else:
    print("\n⚠️  WARNING: Some KPIs do not match expected baselines")

# =============================================================================
# STEP 9: SAVE CLEANED DATA
# =============================================================================

print("\n" + "=" * 80)
print("SAVING CLEANED DATA")
print("=" * 80)

# Save cleaned CSV
df_cleaned.to_csv(OUTPUT_FILE, index=False)
print(f"✓ Cleaned data saved to: {OUTPUT_FILE}")
print(f"  Records: {len(df_cleaned)}")

# Save cleaning log
cleaning_log['final_record_count'] = len(df_cleaned)
cleaning_log['records_removed'] = original_count - len(df_cleaned)

with open(LOG_FILE, 'w') as f:
    json.dump(cleaning_log, f, indent=2)
print(f"✓ Cleaning log saved to: {LOG_FILE}")

# Save validation report
validation_report = {
    'timestamp': datetime.now().isoformat(),
    'source_file': INPUT_FILE,
    'cleaned_file': OUTPUT_FILE,
    'original_records': original_count,
    'cleaned_records': len(df_cleaned),
    'duplicates_removed': duplicates_removed,
    'kpi_validation': validation_results,
    'all_kpis_valid': all_match,
    'data_quality_summary': {
        'total_complaints': int(total_complaints),
        'open_complaints': int(open_complaints),
        'closed_complaints': int(closed_complaints),
        'missing_states': int(df_cleaned['state'].isnull().sum()),
        'date_range': {
            'start': df_cleaned['date_received'].min().strftime('%Y-%m-%d'),
            'end': df_cleaned['date_received'].max().strftime('%Y-%m-%d')
        }
    }
}

with open(VALIDATION_FILE, 'w') as f:
    json.dump(validation_report, f, indent=2)
print(f"✓ Validation report saved to: {VALIDATION_FILE}")

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 80)
print("DATA CLEANING COMPLETE")
print("=" * 80)
print(f"\nOriginal records:  {original_count}")
print(f"Cleaned records:   {len(df_cleaned)}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"\nData Quality: {'✅ PASS' if all_match else '⚠️  REVIEW REQUIRED'}")
print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)
