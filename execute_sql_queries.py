"""
SQL Query Execution and Validation Script
Executes all 9 analytical SQL queries against the cleaned complaints data
"""

import sqlite3
import pandas as pd
import json
from pathlib import Path
from datetime import datetime

# Configuration
DATA_FILE = "data/processed/complaints_cleaned.csv"
SQL_DIR = "sql"
OUTPUT_DIR = "sql/results"

def setup_database():
    """Load cleaned CSV into SQLite in-memory database"""
    print("="*80)
    print("LOADING DATA INTO SQLite DATABASE")
    print("="*80)
    
    # Create in-memory database
    conn = sqlite3.connect(':memory:')
    
    # Load CSV
    df = pd.read_csv(DATA_FILE)
    print(f"✓ Loaded {len(df)} records from {DATA_FILE}")
    
    # Create table
    df.to_sql('complaints_cleaned', conn, index=False, if_exists='replace')
    print(f"✓ Created table 'complaints_cleaned' with {len(df)} rows")
    
    return conn

def execute_query(conn, sql_file):
    """Execute a single SQL query and return results"""
    sql_path = Path(SQL_DIR) / sql_file
    
    with open(sql_path, 'r', encoding='utf-8') as f:
        query = f.read()
    
    # Execute query
    df = pd.read_sql_query(query, conn)
    
    return df

def save_results(df, query_name, output_format='csv'):
    """Save query results to file"""
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)
    
    if output_format == 'csv':
        file_path = output_path / f"{query_name}.csv"
        df.to_csv(file_path, index=False)
    elif output_format == 'json':
        file_path = output_path / f"{query_name}.json"
        df.to_json(file_path, orient='records', indent=2)
    
    return file_path

def validate_kpi_query(df):
    """Validate Query 1 (KPI Summary) against expected baselines"""
    expected = {
        'total_complaints': 4975,
        'open_complaints': 310,
        'closed_complaints': 4665,
        'timely_yes': 4202,
        'timely_no': 463,
        'timely_rate': 90.08,
        'avg_response_days': 8.76
    }
    
    actual = df.iloc[0].to_dict()
    
    validation = {}
    all_valid = True
    
    for key, expected_val in expected.items():
        actual_val = actual.get(key)
        
        # Handle floating point comparison
        if isinstance(expected_val, float):
            match = abs(actual_val - expected_val) < 0.01
        else:
            match = actual_val == expected_val
        
        validation[key] = {
            'expected': expected_val,
            'actual': actual_val,
            'match': match
        }
        
        if not match:
            all_valid = False
    
    return validation, all_valid

def main():
    print("\n" + "="*80)
    print("SQL QUERY EXECUTION PIPELINE")
    print("="*80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Setup database
    conn = setup_database()
    
    # SQL queries to execute
    queries = [
        ('01_kpi_summary.sql', 'kpi_summary', True),  # Validate this one
        ('02_product_analysis.sql', 'product_analysis', False),
        ('03_state_geographic.sql', 'state_geographic', False),
        ('04_channel_effectiveness.sql', 'channel_effectiveness', False),
        ('05_temporal_trends.sql', 'temporal_trends', False),
        ('06_issue_category.sql', 'issue_category', False),
        ('07_company_performance.sql', 'company_performance', False),
        ('08_response_time_distribution.sql', 'response_time_distribution', False),
        ('09_product_issue_matrix.sql', 'product_issue_matrix', False),
    ]
    
    print("\n" + "="*80)
    print("EXECUTING SQL QUERIES")
    print("="*80)
    
    results_summary = []
    
    for sql_file, output_name, validate in queries:
        print(f"\n▶ Executing: {sql_file}")
        
        try:
            # Execute query
            df = execute_query(conn, sql_file)
            row_count = len(df)
            
            # Save results
            csv_path = save_results(df, output_name, 'csv')
            json_path = save_results(df, output_name, 'json')
            
            print(f"  ✓ Rows returned: {row_count}")
            print(f"  ✓ Saved CSV: {csv_path}")
            print(f"  ✓ Saved JSON: {json_path}")
            
            # Validate KPI query
            if validate:
                validation, all_valid = validate_kpi_query(df)
                
                print("\n  KPI VALIDATION:")
                for key, val in validation.items():
                    status = "✓" if val['match'] else "✗"
                    print(f"    {status} {key:20s} Expected: {val['expected']:>10}  Actual: {val['actual']:>10}")
                
                if all_valid:
                    print("  ✅ ALL KPIs MATCH EXPECTED BASELINES")
                else:
                    print("  ❌ KPI MISMATCH DETECTED")
            
            results_summary.append({
                'query': sql_file,
                'output_name': output_name,
                'row_count': row_count,
                'csv_path': str(csv_path),
                'json_path': str(json_path),
                'status': 'success'
            })
            
        except Exception as e:
            print(f"  ✗ ERROR: {str(e)}")
            results_summary.append({
                'query': sql_file,
                'output_name': output_name,
                'error': str(e),
                'status': 'failed'
            })
    
    # Save execution summary
    summary_path = Path(OUTPUT_DIR) / 'execution_summary.json'
    with open(summary_path, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total_queries': len(queries),
            'successful': sum(1 for r in results_summary if r['status'] == 'success'),
            'failed': sum(1 for r in results_summary if r['status'] == 'failed'),
            'queries': results_summary
        }, f, indent=2)
    
    print("\n" + "="*80)
    print("EXECUTION SUMMARY")
    print("="*80)
    print(f"Total queries: {len(queries)}")
    print(f"Successful: {sum(1 for r in results_summary if r['status'] == 'success')}")
    print(f"Failed: {sum(1 for r in results_summary if r['status'] == 'failed')}")
    print(f"\n✓ Summary saved to: {summary_path}")
    
    # Close database
    conn.close()
    
    print("\n" + "="*80)
    print("SQL EXECUTION COMPLETE")
    print("="*80)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
