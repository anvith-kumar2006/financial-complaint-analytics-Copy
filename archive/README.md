# Archive Directory

This directory contains development and audit files that were used during the project's development phase but are no longer needed for production use.

## Files Archived

### Development Scripts (Python)
- `analyze_data.py` - Initial data analysis script
- `data_reconciliation.py` - First reconciliation pass
- `apply_corrections.py` - First correction script
- `second_pass_corrections.py` - Second correction pass
- `third_pass_corrections.py` - Third correction pass
- `final_verification.py` - Final documentation validation

### Audit Reports (JSON)
- `final_verification_report.json` - Final verification results
- `reconciliation_report.json` - Initial reconciliation results
- `second_pass_verification.json` - Second pass verification results

### Documentation (Markdown)
- `RECONCILIATION_REPORT.md` - Reconciliation report documentation

### Data Files
- `lecture-file.csv` - Duplicate of original data (actual original preserved in `data/original/`)

## Purpose

These files were essential for:
1. Ensuring data quality and consistency
2. Validating KPI calculations across documents
3. Achieving 100% documentation accuracy
4. Building confidence in the final deliverables

## Retention

These files are retained for:
- Historical reference
- Audit trail documentation
- Understanding the development process
- Reproducing the validation methodology

## Production Scripts

For production use, refer to:
- `../clean_data.py` - Production data cleaning pipeline
- `../execute_sql_queries.py` - SQL query execution
- `../test_integration.py` - Integration testing suite

---

**Last Updated:** November 24, 2026
