import re

print("=" * 80)
print("APPLYING CORRECTIONS TO PRD AND TRD")
print("=" * 80)

# Read both documents
with open('PRD_Financial_Complaint_Analytics.md', 'r', encoding='utf-8') as f:
    prd_content = f.read()

with open('TRD_Financial_Complaint_Analytics.md', 'r', encoding='utf-8') as f:
    trd_content = f.read()

corrections_applied = []

# =================================================================
# CORRECTION 1: Update KPI baselines to use cleaned data
# =================================================================
print("\n[1] Updating KPI baselines to cleaned data values...")

# Total Complaints
prd_content = re.sub(
    r'(\*\*Current Baseline:\*\*) 4,975 unique complaints \(5,000 total records - 25 duplicates\)',
    r'\1 4,975 unique complaints (after removing 25 duplicates from 5,000 original records)',
    prd_content
)

# Open Complaints  
prd_content = re.sub(
    r'(\*\*Current Baseline:\*\*) 311 \(6\.22% of total\)',
    r'\1 310 (6.23% of total)',
    prd_content
)

# Closed Complaints
prd_content = re.sub(
    r'(\*\*Current Baseline:\*\*) 4,689 \(93\.78% of total\)',
    r'\1 4,665 (93.77% of total)',
    prd_content
)

# Timely Response Rate
prd_content = re.sub(
    r'(\*\*Current Baseline:\*\*) 90\.10% \(4,225 Yes / 4,689 Closed\)',
    r'\1 90.08% (4,202 Yes / 4,665 total = 4,202 Yes + 463 No)',
    prd_content
)

corrections_applied.append("Updated all KPI baselines to cleaned dataset values")

# =================================================================
# CORRECTION 2: Fix "Real-time refresh" to "Manual data reload"
# =================================================================
print("[2] Correcting 'real-time refresh' claims...")

prd_content = re.sub(
    r'(\*\*Refresh:\*\*) Real-time with data updates',
    r'\1 Manual data reload required (static CSV architecture)',
    prd_content,
    flags=re.IGNORECASE
)

corrections_applied.append("Changed 'real-time refresh' to 'manual data reload' for static CSV")

# =================================================================
# CORRECTION 3: Update product distribution to cleaned data
# =================================================================
print("[3] Updating product distribution...")

# Use simple replacements
prd_content = prd_content.replace(
    '- **Expected Distribution:**',
    '- **Expected Distribution (Cleaned Data):**'
)
prd_content = prd_content.replace('Credit card: ~1,194 (23.88%)', 'Credit card: 1,191 (23.94%)')
prd_content = prd_content.replace('Checking or savings account: ~1,060 (21.20%)', 'Checking or savings account: 1,054 (21.19%)')
prd_content = prd_content.replace('Credit reporting: ~912 (18.24%)', 'Credit reporting: 906 (18.21%)')
prd_content = prd_content.replace('Personal loan: ~828 (16.56%)', 'Personal loan: 826 (16.60%)')
prd_content = prd_content.replace('Mortgage: ~653 (13.06%)', 'Mortgage: 648 (13.03%)')
prd_content = prd_content.replace('Buy now, pay later: ~353 (7.06%)', 'Buy now, pay later: 350 (7.04%)')

# Also update in TRD
trd_content = re.sub(
    r'Credit card: 1,194 \(23\.88%\)',
    'Credit card: 1,191 (23.94%)',
    trd_content
)
trd_content = re.sub(
    r'Checking or savings account: 1,060 \(21\.20%\)',
    'Checking or savings account: 1,054 (21.19%)',
    trd_content
)
trd_content = re.sub(
    r'Credit reporting: 912 \(18\.24%\)',
    'Credit reporting: 906 (18.21%)',
    trd_content
)
trd_content = re.sub(
    r'Personal loan: 828 \(16\.56%\)',
    'Personal loan: 826 (16.60%)',
    trd_content
)
trd_content = re.sub(
    r'Mortgage: 653 \(13\.06%\)',
    'Mortgage: 648 (13.03%)',
    trd_content
)
trd_content = re.sub(
    r'Buy now, pay later: 353 \(7\.06%\)',
    'Buy now, pay later: 350 (7.04%)',
    trd_content
)

corrections_applied.append("Updated product distribution to cleaned data values")

# =================================================================
# CORRECTION 4: Update issue categories
# =================================================================
print("[4] Updating issue categories...")

prd_content = prd_content.replace('1. Unexpected fees: ~548', '1. Unexpected fees: 545')
prd_content = prd_content.replace('2. Account access: ~339', '2. Account access: 337')
prd_content = prd_content.replace('3. Fraudulent charges: ~309', '3. Fraudulent charges: 307')
prd_content = prd_content.replace('4. Card declined: ~299', '4. Card declined: 299')
prd_content = prd_content.replace('5. Billing dispute: ~296', '5. Billing dispute: 296')
prd_content = prd_content.replace('6. Transaction dispute: ~287', '6. Transaction dispute: 285')
prd_content = prd_content.replace('7. Account closure: ~260', '7. Account closure: 259')
prd_content = prd_content.replace('8. Report access: ~243', '8. Report access: 242')
prd_content = prd_content.replace('9. Investigation delay: ~229', '9. Incorrect information: 228')
prd_content = prd_content.replace('10. Incorrect information: ~228', '10. Loan servicing: 226')

# Update in TRD too
trd_content = re.sub('Unexpected fees: 548', 'Unexpected fees: 545', trd_content)
trd_content = re.sub('Account access: 339', 'Account access: 337', trd_content)
trd_content = re.sub('Fraudulent charges: 309', 'Fraudulent charges: 307', trd_content)
trd_content = re.sub('Transaction dispute: 287', 'Transaction dispute: 285', trd_content)
trd_content = re.sub('Account closure: 260', 'Account closure: 259', trd_content)
trd_content = re.sub('Report access: 243', 'Report access: 242', trd_content)
trd_content = re.sub('Investigation delay: 229', 'Investigation delay: 226', trd_content)

corrections_applied.append("Updated top 10 issue categories to cleaned data values")

# =================================================================
# CORRECTION 5: Update company distribution
# =================================================================
print("[5] Updating company distribution...")

company_updates = {
    'Harbor Credit: 674': 'Harbor Credit: 669',
    'Silverline Lending: 639': 'Silverline Lending: 637',
    'Atlas Consumer Finance: 633': 'Atlas Consumer Finance: 630',
    'Northstar Financial: 633': 'Northstar Financial: 628',
    'OakBridge Services: 630': 'OakBridge Services: 629',
    'BluePeak Bank: 621': 'BluePeak Bank: 618',
    'Cedar Finance: 605': 'Cedar Finance: 602',
    'Summit Payments: 565': 'Summit Payments: 562',
}

for old, new in company_updates.items():
    prd_content = prd_content.replace(old, new)
    trd_content = trd_content.replace(old, new)

corrections_applied.append("Updated company distribution to cleaned data values")

# =================================================================
# CORRECTION 6: Add company size disclaimer
# =================================================================
print("[6] Adding company size disclaimer...")

# Find company performance chart section and add disclaimer
disclaimer_text = '''- **Important Disclaimer:**
  - Higher complaint volumes do not necessarily indicate poor company performance
  - Company sizes differ significantly
  - Compare timely response rates, not absolute complaint counts
  - Use this chart for relative performance benchmarking only'''

# Insert after Color Coding in company performance chart section
prd_content = re.sub(
    r'(\*\*Color Coding:\*\*\n  - Green: ≥ 90% timely response\n  - Yellow: 80-89% timely response\n  - Red: < 80% timely response)',
    r'\1\n' + disclaimer_text,
    prd_content
)

corrections_applied.append("Added company size disclaimer to company performance chart")

# =================================================================
# CORRECTION 7: Make duplicate removal rule deterministic
# =================================================================
print("[7] Making duplicate removal rule deterministic...")

trd_content = re.sub(
    r'(\*\*Business Rule:\*\*) Keep the earliest received complaint \(by date_received\) when duplicates exist\.',
    r'\1 Keep the first occurrence by row order in original CSV file (pandas keep=\'first\' strategy) when duplicates exist.',
    trd_content
)

corrections_applied.append("Made duplicate removal rule deterministic (keep='first' by row order)")

# =================================================================
# CORRECTION 8: Update version to 1.1 with audit notes
# =================================================================
print("[8] Updating version history...")

version_entry = '''| 1.1 | 2026-11-22 | Product Team | Corrected KPI baselines after data cleaning audit, updated all distributions to cleaned data values, fixed real-time refresh claims |'''

prd_content = re.sub(
    r'(\| 1\.0 \| 2026-11-22 \| Product Team \| Initial PRD based on actual dataset analysis \|)',
    r'\1\n' + version_entry,
    prd_content
)

prd_content = re.sub(
    r'\*\*Version\*\* \| 1\.0 \|',
    '**Version** | 1.1 |',
    prd_content,
    count=1
)

version_entry_trd = '''| 1.1 | 2026-11-22 | Technical Team | Corrected KPI baselines after data cleaning audit, clarified duplicate removal strategy, updated distributions |'''

trd_content = re.sub(
    r'(\| 1\.0 \| 2026-11-22 \| Technical Team \| Initial TRD based on actual dataset analysis \|)',
    r'\1\n' + version_entry_trd,
    trd_content
)

trd_content = re.sub(
    r'\*\*Version\*\* \| 1\.0 \|',
    '**Version** | 1.1 |',
    trd_content,
    count=1
)

corrections_applied.append("Updated version to 1.1 with audit notes in version history")

# =================================================================
# CORRECTION 9: Fix timely response rate denominator clarity
# =================================================================
print("[9] Clarifying timely response rate calculation...")

timely_clarification = '''
   - **Calculation Details:**
     - Numerator: Closed complaints with timely_response = "Yes" (4,202)
     - Denominator: Closed complaints with timely_response = "Yes" OR "No" (4,665)
     - Excludes: Open complaints AND Closed complaints without timely response flag
     - Formula: (4,202 / 4,665) × 100 = 90.08%'''

prd_content = re.sub(
    r'(- \*\*Business Rules:\*\*\n     - Exclude open complaints from calculation\n     - Exclude complaints with missing timely_response values\n     - Display "N/A" if no closed complaints with timely response data)',
    r'\1' + timely_clarification,
    prd_content
)

corrections_applied.append("Added detailed timely response rate calculation breakdown")

# =================================================================
# CORRECTION 10: Update executive summary with corrected baseline
# =================================================================
print("[10] Updating executive summary...")

prd_content = re.sub(
    r'With approximately 5,000 customer complaints',
    'With 4,975 customer complaints (cleaned from 5,000 original records)',
    prd_content
)

prd_content = re.sub(
    r'- Improve timely response rate \(current: 90\.10%\)',
    '- Maintain high timely response rate (current: 90.08%)',
    prd_content
)

corrections_applied.append("Updated executive summary with corrected baseline")

# =================================================================
# Save corrected documents
# =================================================================
print("\n[11] Saving corrected documents...")

with open('PRD_Financial_Complaint_Analytics.md', 'w', encoding='utf-8') as f:
    f.write(prd_content)

with open('TRD_Financial_Complaint_Analytics.md', 'w', encoding='utf-8') as f:
    f.write(trd_content)

print("✓ PRD saved")
print("✓ TRD saved")

# =================================================================
# Summary
# =================================================================
print("\n" + "=" * 80)
print("CORRECTIONS APPLIED SUCCESSFULLY")
print("=" * 80)

for i, correction in enumerate(corrections_applied, 1):
    print(f"{i}. {correction}")

print("\n" + "=" * 80)
print("DOCUMENTS UPDATED TO VERSION 1.1")
print("=" * 80)
print("\nNext Steps:")
print("1. Review updated PRD_Financial_Complaint_Analytics.md")
print("2. Review updated TRD_Financial_Complaint_Analytics.md")
print("3. Review reconciliation_report.json for full audit trail")
print("4. Proceed with implementation using corrected baseline values")
