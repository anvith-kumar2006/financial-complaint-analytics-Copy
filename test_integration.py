"""
Integration Testing Suite
Validates data consistency across all platform components
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime

# Configuration
DATA_FILE = "data/processed/complaints_cleaned.csv"
SQL_RESULTS_DIR = "sql/results"
VALIDATION_LOG = "data/processed/validation_report.json"
OUTPUT_FILE = "test_results.json"

def load_data():
    """Load cleaned CSV data"""
    print("="*80)
    print("LOADING TEST DATA")
    print("="*80)
    
    df = pd.read_csv(DATA_FILE)
    print(f"✓ Loaded {len(df)} records from {DATA_FILE}\n")
    return df

def test_kpi_baselines(df):
    """Test 1: Verify KPI baselines match expected values"""
    print("TEST 1: KPI Baseline Validation")
    print("-"*80)
    
    expected = {
        'total_complaints': 4975,
        'open_complaints': 310,
        'closed_complaints': 4665,
        'timely_yes': 4202,
        'timely_no': 463,
        'timely_rate': 90.08,
        'avg_response_days': 8.76
    }
    
    actual = {
        'total_complaints': len(df),
        'open_complaints': len(df[df['response_status'] == 'Open']),
        'closed_complaints': len(df[df['response_status'] == 'Closed']),
        'timely_yes': len(df[df['timely_response'] == 'Yes']),
        'timely_no': len(df[df['timely_response'] == 'No']),
        'timely_rate': None,
        'avg_response_days': None
    }
    
    # Calculate rates
    if actual['timely_yes'] + actual['timely_no'] > 0:
        actual['timely_rate'] = round((actual['timely_yes'] / (actual['timely_yes'] + actual['timely_no'])) * 100, 2)
    
    closed_with_time = df[(df['response_status'] == 'Closed') & (df['response_time_days'].notna())]
    if len(closed_with_time) > 0:
        actual['avg_response_days'] = round(closed_with_time['response_time_days'].mean(), 2)
    
    # Validate
    results = []
    all_pass = True
    
    for key, expected_val in expected.items():
        actual_val = actual[key]
        
        if isinstance(expected_val, float):
            match = abs(actual_val - expected_val) < 0.01
        else:
            match = actual_val == expected_val
        
        status = "✓ PASS" if match else "✗ FAIL"
        results.append({
            'metric': key,
            'expected': expected_val,
            'actual': actual_val,
            'status': 'pass' if match else 'fail'
        })
        
        print(f"{status} {key:25s} Expected: {expected_val:>10}  Actual: {actual_val:>10}")
        
        if not match:
            all_pass = False
    
    print(f"\nResult: {'✅ ALL TESTS PASSED' if all_pass else '❌ SOME TESTS FAILED'}\n")
    
    return {
        'test_name': 'KPI Baseline Validation',
        'passed': all_pass,
        'total_checks': len(expected),
        'passed_checks': sum(1 for r in results if r['status'] == 'pass'),
        'failed_checks': sum(1 for r in results if r['status'] == 'fail'),
        'details': results
    }

def test_sql_consistency(df):
    """Test 2: Verify SQL query results match Python calculations"""
    print("TEST 2: SQL-Python Consistency Check")
    print("-"*80)
    
    # Load SQL KPI results
    sql_kpi_file = Path(SQL_RESULTS_DIR) / "kpi_summary.json"
    
    if not sql_kpi_file.exists():
        print("✗ SQL results not found\n")
        return {
            'test_name': 'SQL-Python Consistency',
            'passed': False,
            'error': 'SQL results file not found'
        }
    
    with open(sql_kpi_file, 'r') as f:
        sql_results = json.load(f)
    
    sql_kpi = sql_results[0]  # First row contains KPIs
    
    # Python calculations
    python_kpi = {
        'total_complaints': len(df),
        'open_complaints': len(df[df['response_status'] == 'Open']),
        'closed_complaints': len(df[df['response_status'] == 'Closed']),
        'timely_rate': round((len(df[df['timely_response'] == 'Yes']) / 
                             (len(df[df['timely_response'] == 'Yes']) + 
                              len(df[df['timely_response'] == 'No']))) * 100, 2),
        'avg_response_days': round(df[(df['response_status'] == 'Closed') & 
                                      (df['response_time_days'].notna())]['response_time_days'].mean(), 2)
    }
    
    # Compare
    checks = [
        ('total_complaints', sql_kpi['total_complaints'], python_kpi['total_complaints']),
        ('open_complaints', sql_kpi['open_complaints'], python_kpi['open_complaints']),
        ('closed_complaints', sql_kpi['closed_complaints'], python_kpi['closed_complaints']),
        ('timely_rate', sql_kpi['timely_rate'], python_kpi['timely_rate']),
        ('avg_response_days', sql_kpi['avg_response_days'], python_kpi['avg_response_days']),
    ]
    
    results = []
    all_pass = True
    
    for metric, sql_val, python_val in checks:
        if isinstance(sql_val, float):
            match = abs(sql_val - python_val) < 0.01
        else:
            match = sql_val == python_val
        
        status = "✓ PASS" if match else "✗ FAIL"
        results.append({
            'metric': metric,
            'sql_value': sql_val,
            'python_value': python_val,
            'status': 'pass' if match else 'fail'
        })
        
        print(f"{status} {metric:25s} SQL: {sql_val:>10}  Python: {python_val:>10}")
        
        if not match:
            all_pass = False
    
    print(f"\nResult: {'✅ ALL TESTS PASSED' if all_pass else '❌ SOME TESTS FAILED'}\n")
    
    return {
        'test_name': 'SQL-Python Consistency',
        'passed': all_pass,
        'total_checks': len(checks),
        'passed_checks': sum(1 for r in results if r['status'] == 'pass'),
        'failed_checks': sum(1 for r in results if r['status'] == 'fail'),
        'details': results
    }

def test_data_quality(df):
    """Test 3: Data quality and integrity checks"""
    print("TEST 3: Data Quality Checks")
    print("-"*80)
    
    checks = []
    all_pass = True
    
    # Check 1: No duplicate complaint_ids
    duplicates = df['complaint_id'].duplicated().sum()
    dup_pass = duplicates == 0
    checks.append({
        'check': 'No duplicate complaint IDs',
        'expected': 0,
        'actual': duplicates,
        'status': 'pass' if dup_pass else 'fail'
    })
    print(f"{'✓ PASS' if dup_pass else '✗ FAIL'} No duplicate complaint IDs: {duplicates} duplicates")
    if not dup_pass:
        all_pass = False
    
    # Check 2: Valid response status values
    valid_statuses = {'Open', 'Closed'}
    invalid_statuses = df[~df['response_status'].isin(valid_statuses)]
    status_pass = len(invalid_statuses) == 0
    checks.append({
        'check': 'Valid response_status values',
        'expected': 'Open or Closed',
        'actual': len(invalid_statuses),
        'status': 'pass' if status_pass else 'fail'
    })
    print(f"{'✓ PASS' if status_pass else '✗ FAIL'} Valid response_status values: {len(invalid_statuses)} invalid")
    if not status_pass:
        all_pass = False
    
    # Check 3: Open complaints should not have response dates
    open_with_response = df[(df['response_status'] == 'Open') & (df['date_company_responded'].notna())]
    open_pass = len(open_with_response) == 0
    checks.append({
        'check': 'Open complaints without response dates',
        'expected': 0,
        'actual': len(open_with_response),
        'status': 'pass' if open_pass else 'fail'
    })
    print(f"{'✓ PASS' if open_pass else '✗ FAIL'} Open complaints without response dates: {len(open_with_response)} violations")
    if not open_pass:
        all_pass = False
    
    # Check 4: Closed complaints should have response dates
    closed_without_response = df[(df['response_status'] == 'Closed') & (df['date_company_responded'].isna())]
    closed_pass = len(closed_without_response) == 0
    checks.append({
        'check': 'Closed complaints with response dates',
        'expected': 0,
        'actual': len(closed_without_response),
        'status': 'pass' if closed_pass else 'fail'
    })
    print(f"{'✓ PASS' if closed_pass else '✗ FAIL'} Closed complaints with response dates: {len(closed_without_response)} violations")
    if not closed_pass:
        all_pass = False
    
    # Check 5: Date range validity
    df['date_received_parsed'] = pd.to_datetime(df['date_received'])
    date_min = df['date_received_parsed'].min()
    date_max = df['date_received_parsed'].max()
    expected_min = pd.Timestamp('2025-10-01')
    expected_max = pd.Timestamp('2026-10-15')
    date_pass = (date_min >= expected_min) and (date_max <= expected_max)
    checks.append({
        'check': 'Date range within expected bounds',
        'expected': f'{expected_min.date()} to {expected_max.date()}',
        'actual': f'{date_min.date()} to {date_max.date()}',
        'status': 'pass' if date_pass else 'fail'
    })
    print(f"{'✓ PASS' if date_pass else '✗ FAIL'} Date range: {date_min.date()} to {date_max.date()}")
    if not date_pass:
        all_pass = False
    
    print(f"\nResult: {'✅ ALL TESTS PASSED' if all_pass else '❌ SOME TESTS FAILED'}\n")
    
    return {
        'test_name': 'Data Quality Checks',
        'passed': all_pass,
        'total_checks': len(checks),
        'passed_checks': sum(1 for c in checks if c['status'] == 'pass'),
        'failed_checks': sum(1 for c in checks if c['status'] == 'fail'),
        'details': checks
    }

def test_react_data_compatibility():
    """Test 4: Verify React dashboard can parse the CSV"""
    print("TEST 4: React Dashboard Data Compatibility")
    print("-"*80)
    
    react_csv = Path("react-dashboard/public/complaints_cleaned.csv")
    
    if not react_csv.exists():
        print("✗ FAIL: CSV not found in React public folder\n")
        return {
            'test_name': 'React Data Compatibility',
            'passed': False,
            'error': 'CSV file not found in react-dashboard/public/'
        }
    
    # Verify it can be loaded
    try:
        react_df = pd.read_csv(react_csv)
        row_count = len(react_df)
        expected_count = 4975
        
        pass_test = row_count == expected_count
        
        print(f"✓ CSV found in React public folder")
        print(f"{'✓ PASS' if pass_test else '✗ FAIL'} Row count: {row_count} (expected: {expected_count})")
        
        # Check column names match expected format
        expected_columns = [
            'complaint_id', 'date_received', 'financial_product', 'issue_category',
            'issue_detail', 'company_name', 'state', 'submission_channel',
            'response_due_date', 'date_company_responded', 'response_status',
            'company_response', 'timely_response', 'short_complaint_summary',
            'response_time_days'
        ]
        
        columns_match = list(react_df.columns) == expected_columns
        print(f"{'✓ PASS' if columns_match else '✗ FAIL'} Column names match expected format")
        
        overall_pass = pass_test and columns_match
        
        print(f"\nResult: {'✅ ALL TESTS PASSED' if overall_pass else '❌ SOME TESTS FAILED'}\n")
        
        return {
            'test_name': 'React Data Compatibility',
            'passed': overall_pass,
            'checks': {
                'file_exists': True,
                'row_count_match': pass_test,
                'columns_match': columns_match
            }
        }
        
    except Exception as e:
        print(f"✗ FAIL: Error loading CSV: {str(e)}\n")
        return {
            'test_name': 'React Data Compatibility',
            'passed': False,
            'error': str(e)
        }

def main():
    print("\n" + "="*80)
    print("INTEGRATION TEST SUITE")
    print("Financial Complaint Analytics Platform")
    print("="*80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Load data
    df = load_data()
    
    # Run tests
    test_results = []
    
    test_results.append(test_kpi_baselines(df))
    test_results.append(test_sql_consistency(df))
    test_results.append(test_data_quality(df))
    test_results.append(test_react_data_compatibility())
    
    # Summary
    print("="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    total_tests = len(test_results)
    passed_tests = sum(1 for t in test_results if t['passed'])
    failed_tests = total_tests - passed_tests
    
    for i, result in enumerate(test_results, 1):
        status = "✅ PASS" if result['passed'] else "❌ FAIL"
        print(f"{status} Test {i}: {result['test_name']}")
    
    print(f"\nTotal: {total_tests} | Passed: {passed_tests} | Failed: {failed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    # Save results
    output = {
        'timestamp': datetime.now().isoformat(),
        'summary': {
            'total_tests': total_tests,
            'passed': passed_tests,
            'failed': failed_tests,
            'success_rate': round((passed_tests/total_tests)*100, 2)
        },
        'tests': test_results
    }
    
    output_path = Path(OUTPUT_FILE)
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\n✓ Results saved to: {output_path}")
    
    print("\n" + "="*80)
    print("INTEGRATION TESTING COMPLETE")
    print("="*80)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")
    
    # Exit code
    return 0 if failed_tests == 0 else 1

if __name__ == "__main__":
    exit(main())
