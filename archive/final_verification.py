import re
import json
from datetime import datetime

print("=" * 80)
print("FINAL COMPREHENSIVE VERIFICATION")
print("=" * 80)
print(f"Verification Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# AUTHORITATIVE BASELINE VALUES
CORRECT_VALUES = {
    'total_complaints': 4975,
    'open_complaints': 310,
    'open_percentage': 6.23,
    'closed_complaints': 4665,
    'closed_percentage': 93.77,
    'timely_yes': 4202,
    'timely_no': 463,
    'timely_rate': 90.08,
    'avg_response_days': 8.76,
    'median_response_days': 8
}

# Read documents
with open('PRD_Financial_Complaint_Analytics.md', 'r', encoding='utf-8') as f:
    prd_content = f.read()

with open('TRD_Financial_Complaint_Analytics.md', 'r', encoding='utf-8') as f:
    trd_content = f.read()

# =============================================================================
# VERIFICATION 1: Arithmetic Consistency
# =============================================================================

print("=" * 80)
print("VERIFICATION 1: ARITHMETIC CONSISTENCY")
print("=" * 80)

check1 = CORRECT_VALUES['open_complaints'] + CORRECT_VALUES['closed_complaints'] == CORRECT_VALUES['total_complaints']
check2 = CORRECT_VALUES['timely_yes'] + CORRECT_VALUES['timely_no'] == CORRECT_VALUES['closed_complaints']
calculated_rate = round((CORRECT_VALUES['timely_yes'] / CORRECT_VALUES['closed_complaints']) * 100, 2)
check3 = calculated_rate == CORRECT_VALUES['timely_rate']

print(f"\n1. Total = Open + Closed:")
print(f"   {CORRECT_VALUES['open_complaints']} + {CORRECT_VALUES['closed_complaints']} = {CORRECT_VALUES['total_complaints']}")
print(f"   Result: {'✓ PASS' if check1 else '✗ FAIL'}")

print(f"\n2. Closed = Timely Yes + Timely No:")
print(f"   {CORRECT_VALUES['timely_yes']} + {CORRECT_VALUES['timely_no']} = {CORRECT_VALUES['closed_complaints']}")
print(f"   Result: {'✓ PASS' if check2 else '✗ FAIL'}")

print(f"\n3. Timely Response Rate Calculation:")
print(f"   ({CORRECT_VALUES['timely_yes']} / {CORRECT_VALUES['closed_complaints']}) × 100 = {calculated_rate:.2f}%")
print(f"   Expected: {CORRECT_VALUES['timely_rate']}%")
print(f"   Result: {'✓ PASS' if check3 else '✗ FAIL'}")

arithmetic_pass = check1 and check2 and check3

# =============================================================================
# VERIFICATION 2: Scan for Outdated Values
# =============================================================================

print("\n" + "=" * 80)
print("VERIFICATION 2: SCAN FOR OUTDATED VALUES")
print("=" * 80)

# Patterns to search for (INCORRECT values)
incorrect_patterns = {
    '\\b311\\b': ('310', 'Open complaints'),
    '\\b6\\.22%?\\b': ('6.23%', 'Open percentage'),
    '\\b4,689\\b|\\b4689\\b': ('4,665', 'Closed complaints'),
    '\\b93\\.78%?\\b': ('93.77%', 'Closed percentage'),
    '\\b4,225\\b|\\b4225\\b': ('4,202', 'Timely Yes'),
    '\\b464\\b': ('463', 'Timely No'),
    '\\b90\\.10%?\\b': ('90.08%', 'Timely Response Rate'),
}

# Exception contexts (OK to have these values if referring to original data)
exception_contexts = [
    'original',
    'raw csv',
    'before cleaning',
    'total records: 5000',
    '5,000 original',
]

def is_exception_context(line):
    """Check if line refers to original/raw data"""
    line_lower = line.lower()
    return any(exc in line_lower for exc in exception_contexts)

prd_issues = []
trd_issues = []

# Scan PRD
prd_lines = prd_content.split('\n')
for pattern, (correct, desc) in incorrect_patterns.items():
    for i, line in enumerate(prd_lines, 1):
        if re.search(pattern, line) and not is_exception_context(line):
            prd_issues.append({
                'line': i,
                'description': desc,
                'found': re.search(pattern, line).group(),
                'should_be': correct,
                'context': line.strip()[:100]
            })

# Scan TRD
trd_lines = trd_content.split('\n')
for pattern, (correct, desc) in incorrect_patterns.items():
    for i, line in enumerate(trd_lines, 1):
        if re.search(pattern, line) and not is_exception_context(line):
            trd_issues.append({
                'line': i,
                'description': desc,
                'found': re.search(pattern, line).group(),
                'should_be': correct,
                'context': line.strip()[:100]
            })

print(f"\nPRD Scan Results:")
if prd_issues:
    print(f"  ✗ Found {len(prd_issues)} outdated value(s):")
    for issue in prd_issues:
        print(f"    Line {issue['line']}: {issue['description']} = '{issue['found']}' (should be '{issue['should_be']}')")
        print(f"      Context: {issue['context']}")
else:
    print(f"  ✓ No outdated values found")

print(f"\nTRD Scan Results:")
if trd_issues:
    print(f"  ✗ Found {len(trd_issues)} outdated value(s):")
    for issue in trd_issues:
        print(f"    Line {issue['line']}: {issue['description']} = '{issue['found']}' (should be '{issue['should_be']}')")
        print(f"      Context: {issue['context']}")
else:
    print(f"  ✓ No outdated values found")

outdated_values_pass = len(prd_issues) == 0 and len(trd_issues) == 0

# =============================================================================
# VERIFICATION 3: KPI Formula Consistency (PRD and TRD)
# =============================================================================

print("\n" + "=" * 80)
print("VERIFICATION 3: KPI FORMULA CONSISTENCY")
print("=" * 80)

# Check if DAX formulas are present and correct
dax_checks = []

# Total Complaints
if 'DISTINCTCOUNT(Complaints[complaint_id])' in prd_content or 'DISTINCTCOUNT(Complaints[complaint_id])' in trd_content:
    dax_checks.append(('Total Complaints DAX', True))
else:
    dax_checks.append(('Total Complaints DAX', False))

# Timely Response Rate
if 'Timely Response Rate' in prd_content and 'TimelyYes' in prd_content and 'TimelyNo' in prd_content:
    dax_checks.append(('Timely Response Rate DAX', True))
else:
    dax_checks.append(('Timely Response Rate DAX', False))

# Average Response Time
if 'AVERAGE(Complaints[response_time_days])' in prd_content or 'AVERAGE(Complaints[response_time_days])' in trd_content:
    dax_checks.append(('Average Response Time DAX', True))
else:
    dax_checks.append(('Average Response Time DAX', False))

print("\nDAX Formula Presence:")
for check_name, passed in dax_checks:
    print(f"  {'✓' if passed else '✗'} {check_name}")

formulas_pass = all(passed for _, passed in dax_checks)

# =============================================================================
# VERIFICATION 4: Terminology Consistency
# =============================================================================

print("\n" + "=" * 80)
print("VERIFICATION 4: TERMINOLOGY CONSISTENCY")
print("=" * 80)

# Check for problematic terminology
terminology_issues = []

# "Real-time" should be replaced with "manual reload" context
realtime_occurrences_prd = len(re.findall(r'\breal-?time\b', prd_content, re.IGNORECASE))
realtime_occurrences_trd = len(re.findall(r'\breal-?time\b', trd_content, re.IGNORECASE))

# Check if "manual data reload" or similar is present
manual_reload_prd = 'manual data reload' in prd_content.lower() or 'manual reload' in prd_content.lower()
manual_reload_trd = 'manual data reload' in trd_content.lower() or 'manual reload' in trd_content.lower()

print(f"\nReal-time terminology:")
print(f"  PRD: {realtime_occurrences_prd} occurrence(s)")
print(f"  TRD: {realtime_occurrences_trd} occurrence(s)")
print(f"  Note: Some 'real-time' references may be acceptable in context (e.g., 'not real-time')")

print(f"\nManual reload terminology:")
print(f"  PRD: {'✓ Present' if manual_reload_prd else '✗ Not found'}")
print(f"  TRD: {'✓ Present' if manual_reload_trd else '✗ Not found'}")

terminology_pass = manual_reload_prd and manual_reload_trd

# =============================================================================
# VERIFICATION 5: Document Agreement (PRD vs TRD)
# =============================================================================

print("\n" + "=" * 80)
print("VERIFICATION 5: DOCUMENT AGREEMENT")
print("=" * 80)

# Extract key baseline values from both documents
def extract_baseline(content, pattern, description):
    match = re.search(pattern, content)
    if match:
        return match.group(1) if match.lastindex else match.group()
    return None

agreement_checks = [
    ('Total Complaints', r'4,?975', r'4,?975'),
    ('Open Complaints', r'\b310\b', r'\b310\b'),
    ('Closed Complaints', r'4,?665', r'4,?665'),
    ('Timely Rate', r'90\.08%', r'90\.08%'),
]

print(f"\nBaseline Value Agreement:")
agreement_pass = True
for desc, prd_pattern, trd_pattern in agreement_checks:
    prd_has = bool(re.search(prd_pattern, prd_content))
    trd_has = bool(re.search(trd_pattern, trd_content))
    agree = prd_has and trd_has
    print(f"  {'✓' if agree else '✗'} {desc}: PRD={'✓' if prd_has else '✗'}, TRD={'✓' if trd_has else '✗'}")
    if not agree:
        agreement_pass = False

# =============================================================================
# FINAL ASSESSMENT
# =============================================================================

print("\n" + "=" * 80)
print("FINAL ASSESSMENT")
print("=" * 80)

all_checks = [
    ('Arithmetic Consistency', arithmetic_pass),
    ('No Outdated Values', outdated_values_pass),
    ('KPI Formulas Present', formulas_pass),
    ('Terminology Updated', terminology_pass),
    ('PRD/TRD Agreement', agreement_pass),
]

print(f"\nVerification Results:")
for check_name, passed in all_checks:
    print(f"  {'✓' if passed else '✗'} {check_name}")

all_pass = all(passed for _, passed in all_checks)

if all_pass:
    print(f"\n" + "=" * 80)
    print(f"✅ ALL VERIFICATIONS PASSED")
    print(f"=" * 80)
    print(f"\nDocuments are ready for implementation:")
    print(f"  - PRD_Financial_Complaint_Analytics.md (v1.1)")
    print(f"  - TRD_Financial_Complaint_Analytics.md (v1.1)")
    print(f"\nBaseline Values Confirmed:")
    print(f"  Total Complaints:        4,975")
    print(f"  Open Complaints:         310 (6.23%)")
    print(f"  Closed Complaints:       4,665 (93.77%)")
    print(f"  Timely Yes:              4,202")
    print(f"  Timely No:               463")
    print(f"  Timely Response Rate:    90.08%")
    print(f"  Average Response Time:   8.76 days")
else:
    print(f"\n" + "=" * 80)
    print(f"⚠️  VERIFICATION INCOMPLETE")
    print(f"=" * 80)
    print(f"\nIssues remaining:")
    for check_name, passed in all_checks:
        if not passed:
            print(f"  - {check_name}")

# =============================================================================
# SAVE VERIFICATION REPORT
# =============================================================================

verification_report = {
    "verification_date": datetime.now().isoformat(),
    "baseline_values": CORRECT_VALUES,
    "arithmetic_consistency": {
        "total_equals_open_plus_closed": check1,
        "closed_equals_timely_yes_plus_no": check2,
        "timely_rate_calculation_correct": check3,
        "all_passed": arithmetic_pass
    },
    "outdated_values_scan": {
        "prd_issues": prd_issues,
        "trd_issues": trd_issues,
        "all_corrected": outdated_values_pass
    },
    "kpi_formulas": {
        "checks": [{"name": name, "passed": passed} for name, passed in dax_checks],
        "all_present": formulas_pass
    },
    "terminology": {
        "realtime_occurrences_prd": realtime_occurrences_prd,
        "realtime_occurrences_trd": realtime_occurrences_trd,
        "manual_reload_mentioned": terminology_pass
    },
    "document_agreement": {
        "checks": [{"description": desc, "passed": bool(re.search(prd_pat, prd_content)) and bool(re.search(trd_pat, trd_content))} 
                   for desc, prd_pat, trd_pat in agreement_checks],
        "all_agree": agreement_pass
    },
    "final_status": "PASS" if all_pass else "FAIL",
    "ready_for_implementation": all_pass
}

with open('final_verification_report.json', 'w') as f:
    json.dump(verification_report, f, indent=2)

print(f"\n✓ Verification report saved to: final_verification_report.json")

print("\n" + "=" * 80)
