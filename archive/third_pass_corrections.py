import re

print("=" * 80)
print("THIRD-PASS: FINAL MANUAL CORRECTIONS")
print("=" * 80)

# Read documents
with open('PRD_Financial_Complaint_Analytics.md', 'r', encoding='utf-8') as f:
    prd_content = f.read()

with open('TRD_Financial_Complaint_Analytics.md', 'r', encoding='utf-8') as f:
    trd_content = f.read()

corrections = []

# =============================================================================
# PRD REMAINING ISSUES (Lines: 1362, 1378, 1379, 1380, 1274)
# =============================================================================

print("\n[PRD Corrections]")

# Issue 1: Testing requirements section (around line 1362, 1378-1380)
print("  [1] Correcting testing validation baselines...")

# Find and replace in testing section - look for the pattern
prd_content = re.sub(
    r'Total Complaints: 4,975 \(unique\)[\s\S]{0,200}Open Complaints: 311 \(6\.22%\)',
    'Total Complaints: 4,975 (unique)\n  - Open Complaints: 310 (6.23%)',
    prd_content
)

prd_content = re.sub(
    r'Closed Complaints: 4,689 \(93\.78%\)',
    'Closed Complaints: 4,665 (93.77%)',
    prd_content
)

prd_content = re.sub(
    r'Timely Response Rate: 90\.10%',
    'Timely Response Rate: 90.08%',
    prd_content
)

corrections.append("Corrected testing validation baselines")

# Issue 2: Line 1274 - in performance metrics or acceptance criteria
print("  [2] Searching for remaining 90.10% references...")

# More aggressive replacement of 90.10%
prd_content = prd_content.replace('90.10%', '90.08%')
corrections.append("Replaced all remaining 90.10% with 90.08%")

# Issue 3: Replace any remaining 311, 4,689, 93.78%, 6.22% in non-raw-data contexts
print("  [3] Context-aware replacements...")

# These should be safe in acceptance criteria and testing sections
prd_content = re.sub(
    r'(\bOpen:?\s*)\s*311\b',
    r'\g<1>310',
    prd_content
)

prd_content = re.sub(
    r'(\bClosed:?\s*)\s*4,689\b',
    r'\g<1>4,665',
    prd_content
)

prd_content = re.sub(
    r'(\bClosed:?\s*)\s*4689\b',
    r'\g<1>4665',
    prd_content
)

prd_content = re.sub(
    r'311\s*\(6\.22%\)',
    '310 (6.23%)',
    prd_content
)

prd_content = re.sub(
    r'4,689\s*\(93\.78%\)',
    '4,665 (93.77%)',
    prd_content
)

prd_content = re.sub(
    r'4689\s*\(93\.78%\)',
    '4665 (93.77%)',
    prd_content
)

corrections.append("Applied context-aware replacements for remaining values")

# =============================================================================
# TRD REMAINING ISSUES (Lines: 413, 497, 578 - all related to 311 and 6.22%)
# =============================================================================

print("\n[TRD Corrections]")

print("  [1] Correcting column 10 and 13 Null Count references...")

# These are in data dictionary - Null Count fields
trd_content = re.sub(
    r'(\*\*Null Count\*\* \|) 311 \(6\.22%\)',
    r'\g<1> 310 (6.23%)',
    trd_content
)

corrections.append("Corrected Null Count references in TRD data dictionary")

print("  [2] Correcting whitespace issues count...")

# This might be in the data quality issues section referring to Open complaints
trd_content = re.sub(
    r'(\|\s*\*\*Open complaints without response dates\*\*\s*\|)\s*311\s*\|\s*6\.22%',
    r'\g<1> 310 | 6.23%',
    trd_content
)

corrections.append("Corrected data quality issues table")

print("  [3] Final sweep of 311 and 6.22%...")

# Final aggressive replacements in TRD for remaining instances
# Be careful not to replace in "original data" contexts
lines = trd_content.split('\n')
for i, line in enumerate(lines):
    # Skip lines that explicitly mention "original" or "raw"
    if 'original' in line.lower() or 'raw' in line.lower() or 'before' in line.lower():
        continue
    
    # Replace 311 references
    if '311' in line and '310' not in line:
        lines[i] = line.replace('311', '310')
    
    # Replace 6.22% references
    if '6.22%' in line or '6.22 %' in line:
        lines[i] = lines[i].replace('6.22%', '6.23%').replace('6.22 %', '6.23%')

trd_content = '\n'.join(lines)
corrections.append("Applied final sweep for 311 and 6.22% in TRD")

# =============================================================================
# VERIFICATION SCAN
# =============================================================================

print("\n[Verification Scan]")

# Count remaining issues
incorrect_patterns = {
    'PRD': {
        '\\b311\\b': 'open complaints',
        '\\b6\\.22%?\\b': 'open percentage',
        '\\b4,689\\b': 'closed complaints',
        '\\b4689\\b': 'closed complaints',
        '\\b93\\.78%?\\b': 'closed percentage',
        '\\b90\\.10%?\\b': 'timely rate',
    },
    'TRD': {
        '\\b311\\b': 'open complaints',
        '\\b6\\.22%?\\b': 'open percentage',
        '\\b4,689\\b': 'closed complaints',
        '\\b4689\\b': 'closed complaints',
        '\\b93\\.78%?\\b': 'closed percentage',
        '\\b4,225\\b': 'timely yes',
        '\\b464\\b': 'timely no',
        '\\b90\\.10%?\\b': 'timely rate',
    }
}

# Exception patterns (these are OK to keep - referring to original data)
exceptions = [
    '5,000 original',
    '5000 original',
    'raw CSV',
    'before cleaning',
    'original data',
    'Total records: 5000',
    'Total Records:** | 5,000',
]

def should_skip(line, exceptions):
    """Check if line should be skipped (contains exception patterns)"""
    line_lower = line.lower()
    return any(exc.lower() in line_lower for exc in exceptions)

prd_remaining = {}
for pattern, desc in incorrect_patterns['PRD'].items():
    matches = []
    for i, line in enumerate(prd_content.split('\n'), 1):
        if re.search(pattern, line) and not should_skip(line, exceptions):
            matches.append((i, line.strip()[:80]))
    if matches:
        prd_remaining[desc] = matches

trd_remaining = {}
for pattern, desc in incorrect_patterns['TRD'].items():
    matches = []
    for i, line in enumerate(trd_content.split('\n'), 1):
        if re.search(pattern, line) and not should_skip(line, exceptions):
            matches.append((i, line.strip()[:80]))
    if matches:
        trd_remaining[desc] = matches

if prd_remaining:
    print(f"\n  ⚠️  PRD still has {len(prd_remaining)} issue types:")
    for desc, matches in prd_remaining.items():
        print(f"    - {desc}: {len(matches)} occurrence(s)")
        for line_num, text in matches[:2]:
            print(f"      Line {line_num}: {text}")
else:
    print(f"\n  ✓ PRD: All incorrect values corrected!")

if trd_remaining:
    print(f"\n  ⚠️  TRD still has {len(trd_remaining)} issue types:")
    for desc, matches in trd_remaining.items():
        print(f"    - {desc}: {len(matches)} occurrence(s)")
        for line_num, text in matches[:2]:
            print(f"      Line {line_num}: {text}")
else:
    print(f"\n  ✓ TRD: All incorrect values corrected!")

# =============================================================================
# SAVE FILES
# =============================================================================

print("\n[Saving Corrected Files]")

with open('PRD_Financial_Complaint_Analytics.md', 'w', encoding='utf-8') as f:
    f.write(prd_content)
print("  ✓ PRD saved")

with open('TRD_Financial_Complaint_Analytics.md', 'w', encoding='utf-8') as f:
    f.write(trd_content)
print("  ✓ TRD saved")

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 80)
print("THIRD-PASS COMPLETE")
print("=" * 80)

print(f"\nCorrections Applied: {len(corrections)}")
for i, correction in enumerate(corrections, 1):
    print(f"  {i}. {correction}")

if not prd_remaining and not trd_remaining:
    print("\n✅ SUCCESS: ALL incorrect values have been corrected!")
    print("   Both PRD and TRD now use consistent baseline values:")
    print(f"   - Total: 4,975")
    print(f"   - Open: 310 (6.23%)")
    print(f"   - Closed: 4,665 (93.77%)")
    print(f"   - Timely Yes: 4,202")
    print(f"   - Timely No: 463")
    print(f"   - Timely Rate: 90.08%")
    print(f"   - Avg Response: 8.76 days")
else:
    total_issues = sum(len(matches) for matches in prd_remaining.values()) + sum(len(matches) for matches in trd_remaining.values())
    print(f"\n⚠️  {total_issues} issues remaining - manual review required")

print("\n" + "=" * 80)
