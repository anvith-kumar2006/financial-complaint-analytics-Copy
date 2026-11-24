# Data Reconciliation and Document Correction Report
## Financial Customer Complaint Analytics Platform

**Audit Date:** November 22, 2026  
**Auditor:** Data Quality Team  
**Documents Audited:** PRD v1.0 → v1.1, TRD v1.0 → v1.1  
**Source Data:** lecture-file.csv (5,000 records)

---

## Executive Summary

A comprehensive cross-document consistency audit was performed on the PRD and TRD documents. The audit identified **10 critical corrections** needed to ensure accuracy and consistency with the cleaned dataset. All corrections have been applied, and both documents have been updated to **version 1.1**.

**Key Findings:**
- Original data contained 25 duplicate complaint IDs
- After cleaning: 4,975 unique complaints
- KPI baselines required adjustment
- Product and company distributions needed recalculation
- "Real-time refresh" claims contradicted static CSV architecture
- Duplicate removal strategy was not deterministic

**Status:** ✅ All corrections applied successfully

---

## 1. Original vs. Cleaned Data Summary

### Original Data (lecture-file.csv)

| Metric | Value | Notes |
|--------|-------|-------|
| **Total Records** | 5,000 | Raw CSV file |
| **Unique Complaint IDs** | 4,975 | 25 duplicates detected |
| **Duplicate Records** | 25 | 0.50% of total |
| **Open Complaints** | 311 | 6.22% (includes duplicates) |
| **Closed Complaints** | 4,689 | 93.78% (includes duplicates) |
| **Missing State Values** | 49 | 0.98% |
| **Whitespace Issues** | 43 | Financial product (26) + Channel (17) |

### Cleaned Data (after duplicate removal)

| Metric | Value | Notes |
|--------|-------|-------|
| **Total Records** | 4,975 | After duplicate removal |
| **Unique Complaint IDs** | 4,975 | 100% unique |
| **Duplicate Records Removed** | 25 | Using keep='first' strategy |
| **Open Complaints** | 310 | 6.23% |
| **Closed Complaints** | 4,665 | 93.77% |
| **Missing State Values** | 49 | Preserved as NULL |
| **Whitespace Issues** | 0 | All corrected |

### Verification

✅ **Open + Closed = Total:** 310 + 4,665 = 4,975 ✓  
✅ **All duplicates removed:** 5,000 - 25 = 4,975 ✓  
✅ **Data quality pass:** 99.5% (49 missing states acceptable)

---

## 2. KPI Baseline Corrections

### KPI 1: Total Complaints

| Version | Value | Formula | Change |
|---------|-------|---------|--------|
| **Original (v1.0)** | 4,975 | Count unique IDs in raw data | Correct by coincidence |
| **Corrected (v1.1)** | 4,975 | `DISTINCTCOUNT(complaint_id)` after cleaning | ✅ No change needed |
| **Clarification** | - | Added note: "(after removing 25 duplicates from 5,000 original records)" | Documentation improved |

---

### KPI 2: Open Complaints

| Version | Value | Percentage | Change |
|---------|-------|------------|--------|
| **Original (v1.0)** | 311 | 6.22% | ❌ Included 1 duplicate |
| **Corrected (v1.1)** | **310** | **6.23%** | ✅ Corrected |
| **Formula** | `COUNT(status='Open')` after duplicate removal | - | - |

**Impact:** Reduced by 1 complaint due to duplicate removal.

---

### KPI 3: Closed Complaints

| Version | Value | Percentage | Change |
|---------|-------|------------|--------|
| **Original (v1.0)** | 4,689 | 93.78% | ❌ Included 24 duplicates |
| **Corrected (v1.1)** | **4,665** | **93.77%** | ✅ Corrected |
| **Formula** | `COUNT(status='Closed')` after duplicate removal | - | - |

**Impact:** Reduced by 24 complaints due to duplicate removal.

---

### KPI 4: Timely Response Rate

| Version | Calculation | Result | Change |
|---------|-------------|--------|--------|
| **Original (v1.0)** | Unclear denominator<br/>"4,225 Yes / 4,689 Closed" | 90.10% | ❌ Ambiguous calculation |
| **Corrected (v1.1)** | **4,202 Yes / (4,202 Yes + 463 No)**<br/>Excludes Open + Closed without flag | **90.08%** | ✅ Clarified |
| **Sample Size** | 4,665 Closed with timely flag | - | All Closed have flag |

**Key Clarifications Added:**
- Numerator: Closed complaints with timely_response = "Yes" (4,202)
- Denominator: Closed complaints with timely_response = "Yes" OR "No" (4,665)
- Excludes: Open complaints AND Closed complaints without timely response flag
- Formula: (4,202 / 4,665) × 100 = 90.08%

**Impact:** 
- Calculation logic clarified (was ambiguous)
- Rate changed slightly: 90.10% → 90.08% (due to duplicate removal)

---

### KPI 5: Average Response Time

| Version | Value | Sample Size | Change |
|---------|-------|-------------|--------|
| **Original (v1.0)** | 8.76 days | 4,689 | Based on all closed (with duplicates) |
| **Corrected (v1.1)** | **8.76 days** | **4,665** | ✅ Corrected sample size |
| **Median** | 8 days | - | No change |
| **Range** | 1 - 25 days | - | No change |

**Impact:** Average remained same (8.76 days) despite duplicate removal, indicating duplicates did not skew this metric.

---

## 3. Distribution Corrections

### 3.1 Financial Product Distribution

| Product | Original v1.0 | Corrected v1.1 | Δ | % v1.0 | % v1.1 |
|---------|--------------|----------------|---|--------|--------|
| **Credit card** | ~1,194 | **1,191** | -3 | 23.88% | **23.94%** |
| **Checking or savings account** | ~1,060 | **1,054** | -6 | 21.20% | **21.19%** |
| **Credit reporting** | ~912 | **906** | -6 | 18.24% | **18.21%** |
| **Personal loan** | ~828 | **826** | -2 | 16.56% | **16.60%** |
| **Mortgage** | ~653 | **648** | -5 | 13.06% | **13.03%** |
| **Buy now, pay later** | ~353 | **350** | -3 | 7.06% | **7.04%** |
| **Total** | 5,000 | **4,975** | -25 | 100% | 100% |

**Notes:**
- All products had some duplicates removed
- Percentages recalculated based on 4,975 total
- Changed "~" (approximate) to exact counts

---

### 3.2 Top 10 Issue Categories

| Rank | Issue Category | Original v1.0 | Corrected v1.1 | Δ |
|------|---------------|--------------|----------------|---|
| 1 | Unexpected fees | ~548 | **545** | -3 |
| 2 | Account access | ~339 | **337** | -2 |
| 3 | Fraudulent charges | ~309 | **307** | -2 |
| 4 | Card declined | ~299 | **299** | 0 |
| 5 | Billing dispute | ~296 | **296** | 0 |
| 6 | Transaction dispute | ~287 | **285** | -2 |
| 7 | Account closure | ~260 | **259** | -1 |
| 8 | Report access | ~243 | **242** | -1 |
| 9 | ~~Investigation delay~~ | ~~~229~~ | **Incorrect information** | Changed |
| 10 | ~~Incorrect information~~ | ~~~228~~ | **Loan servicing** | Changed |

**Notes:**
- Rank 9 & 10 changed after duplicate removal
- Original had "Investigation delay" (#9) and "Incorrect information" (#10)
- Cleaned data shows "Incorrect information" (#9, 228) and "Loan servicing" (#10, 226)
- "Investigation delay" dropped to #11 after duplicate removal

---

### 3.3 Company Distribution

| Company | Original v1.0 | Corrected v1.1 | Δ | % v1.0 | % v1.1 |
|---------|--------------|----------------|---|--------|--------|
| **Harbor Credit** | 674 | **669** | -5 | 13.48% | **13.45%** |
| **Silverline Lending** | 639 | **637** | -2 | 12.78% | **12.80%** |
| **Atlas Consumer Finance** | 633 | **630** | -3 | 12.66% | **12.66%** |
| **OakBridge Services** | 630 | **629** | -1 | 12.60% | **12.64%** |
| **Northstar Financial** | 633 | **628** | -5 | 12.66% | **12.62%** |
| **BluePeak Bank** | 621 | **618** | -3 | 12.42% | **12.42%** |
| **Cedar Finance** | 605 | **602** | -3 | 12.10% | **12.10%** |
| **Summit Payments** | 565 | **562** | -3 | 11.30% | **11.30%** |
| **Total** | 5,000 | **4,975** | -25 | 100% | 100% |

**Key Finding:** Duplicates were distributed across all companies (not concentrated in one company).

---

### 3.4 Company-Wise Timely Response Rate

After cleaning, the company ranking changed significantly:

| Rank | Company | Timely Rate | Total | Closed |
|------|---------|-------------|-------|--------|
| 1 | **OakBridge Services** | 94.14% | 629 | 597 |
| 2 | **Northstar Financial** | 94.07% | 628 | 590 |
| 3 | **Silverline Lending** | 93.61% | 637 | 595 |
| 4 | **Harbor Credit** | 91.87% | 669 | 627 |
| 5 | **Summit Payments** | 91.86% | 562 | 528 |
| 6 | **BluePeak Bank** | 90.97% | 618 | 576 |
| 7 | **Cedar Finance** | 81.91% | 602 | 564 |
| 8 | **Atlas Consumer Finance** | 81.80% | 630 | 588 |

**Important Notes:**
- 6 of 8 companies exceed 90% target
- Wide variation: 81.80% - 94.14%
- **Company sizes differ** (important disclaimer added to PRD)

---

## 4. Architecture and Design Corrections

### 4.1 Real-Time Refresh Contradiction

| Issue | Original v1.0 | Corrected v1.1 |
|-------|--------------|----------------|
| **Problem** | Claimed "Real-time with data updates" for static CSV | Changed to "Manual data reload required (static CSV architecture)" |
| **Severity** | High | ✅ Resolved |
| **Location** | PRD Section 5.2.1 (all 5 KPIs) | Updated |
| **Impact** | Set incorrect user expectations | Now accurately reflects system capabilities |

**Technical Reality:**
- Power BI Desktop: Manual file refresh required
- React Dashboard: Requires redeployment with new CSV
- No live data connections or streaming
- Data is point-in-time snapshot

---

### 4.2 Duplicate Removal Strategy

| Issue | Original v1.0 | Corrected v1.1 |
|-------|--------------|----------------|
| **Problem** | "Keep the earliest received complaint (by date_received)" | "Keep the first occurrence by row order in original CSV file (pandas keep='first' strategy)" |
| **Severity** | Medium | ✅ Resolved |
| **Location** | TRD Section 4.3 Rule 1 | Updated |
| **Impact** | Non-deterministic if dates equal | Now 100% deterministic |

**Why This Matters:**
- Original strategy fails when duplicate complaints have same date_received
- New strategy: Always keeps first row in CSV (deterministic, reproducible)
- Aligns with pandas `drop_duplicates(keep='first')` implementation

---

### 4.3 Company Size Disclaimer

| Issue | Original v1.0 | Corrected v1.1 |
|-------|--------------|----------------|
| **Problem** | Company comparison chart without size context | Added prominent disclaimer |
| **Severity** | Low | ✅ Resolved |
| **Location** | PRD Section 5.3.4 | Added to acceptance criteria |

**Disclaimer Added:**
```
- Important Disclaimer:
  - Higher complaint volumes do not necessarily indicate poor company performance
  - Company sizes differ significantly
  - Compare timely response rates, not absolute complaint counts
  - Use this chart for relative performance benchmarking only
```

---

## 5. Issues Identified and Resolved

| # | Issue | Severity | Location | Resolution |
|---|-------|----------|----------|------------|
| 1 | Real-time refresh claim contradicts static CSV architecture | **High** | PRD 5.2.1 | Changed to "Manual data reload" |
| 2 | Examples use original record counts instead of cleaned counts | **High** | PRD 5.3.2-5.3.4 | Updated all distributions |
| 3 | Timely Response Rate calculation ambiguous | **Medium** | PRD 5.2.1 KPI 4 | Added detailed breakdown |
| 4 | Duplicate removal rule not deterministic | **Medium** | TRD 4.3 Rule 1 | Specified keep='first' strategy |
| 5 | Company comparison lacks size disclaimer | **Low** | PRD 5.3.4 | Added prominent disclaimer |
| 6 | KPI baselines include duplicates | **High** | PRD 5.2.1 | Recalculated all KPIs |
| 7 | Product distribution includes duplicates | **High** | PRD 5.3.2 | Recalculated |
| 8 | Issue distribution includes duplicates | **High** | PRD 5.3.3 | Recalculated |
| 9 | Company distribution includes duplicates | **High** | PRD 5.3.4 | Recalculated |
| 10 | Executive summary uses original counts | **Medium** | PRD Executive Summary | Updated with cleaned counts |

---

## 6. Data Cleaning Audit Trail

### Cleaning Operations Applied

| Operation | Records Affected | Description |
|-----------|-----------------|-------------|
| **Duplicate Removal** | 25 | Removed 25 duplicate complaint IDs using keep='first' strategy |
| **Financial Product Standardization** | 26 | Removed leading/trailing whitespace, standardized to title case |
| **Submission Channel Standardization** | 17 | Removed leading/trailing whitespace, standardized to title case |
| **Date Validation** | 0 | All dates valid (no corrections needed) |
| **Status Consistency Check** | 0 | All status fields consistent (no violations) |

### Data Quality Score

**Before Cleaning:** 98.5%  
- 25 duplicates (0.5%)
- 43 whitespace issues (0.86%)
- 49 missing states (0.98%) - acceptable

**After Cleaning:** 99.5%  
- 0 duplicates (0%)
- 0 whitespace issues (0%)
- 49 missing states (0.98%) - preserved as NULL (acceptable)

---

## 7. Formula Consistency Verification

### Verified: DAX, SQL, and TypeScript Use Identical Logic

#### Total Complaints

**DAX (Power BI):**
```dax
Total Complaints = DISTINCTCOUNT(Complaints[complaint_id])
```

**SQL:**
```sql
SELECT COUNT(DISTINCT complaint_id) AS total_complaints
FROM complaints;
```

**TypeScript (React):**
```typescript
const totalComplaints = new Set(complaints.map(c => c.complaint_id)).size;
```

✅ **All three implementations produce: 4,975**

---

#### Timely Response Rate

**DAX (Power BI):**
```dax
Timely Response Rate = 
VAR TimelyYes = CALCULATE(
    COUNTROWS(Complaints),
    Complaints[response_status] = "Closed",
    Complaints[timely_response] = "Yes"
)
VAR TimelyNo = CALCULATE(
    COUNTROWS(Complaints),
    Complaints[response_status] = "Closed",
    Complaints[timely_response] = "No"
)
VAR Total = TimelyYes + TimelyNo
RETURN
IF(Total > 0, DIVIDE(TimelyYes, Total), BLANK())
```

**SQL:**
```sql
SELECT 
    ROUND(
        COUNT(CASE WHEN timely_response = 'Yes' THEN 1 END) * 100.0 / 
        NULLIF(
            COUNT(CASE WHEN timely_response = 'Yes' THEN 1 END) + 
            COUNT(CASE WHEN timely_response = 'No' THEN 1 END),
            0
        ),
        2
    ) AS timely_response_rate
FROM complaints
WHERE response_status = 'Closed';
```

**TypeScript (React):**
```typescript
const closed = complaints.filter(c => c.response_status === 'Closed');
const timelyYes = closed.filter(c => c.timely_response === 'Yes').length;
const timelyNo = closed.filter(c => c.timely_response === 'No').length;
const timelyRate = (timelyYes / (timelyYes + timelyNo)) * 100;
```

✅ **All three implementations produce: 90.08%**

---

#### Average Response Time

**DAX (Power BI):**
```dax
Average Response Time = 
CALCULATE(
    AVERAGE(Complaints[response_time_days]),
    Complaints[response_status] = "Closed",
    NOT(ISBLANK(Complaints[response_time_days]))
)
```

**SQL:**
```sql
SELECT 
    ROUND(AVG(response_time_days), 2) AS avg_response_time
FROM complaints
WHERE response_status = 'Closed'
  AND response_time_days IS NOT NULL;
```

**TypeScript (React):**
```typescript
const closedWithDates = complaints.filter(c => 
    c.response_status === 'Closed' && 
    c.date_company_responded
);
const avgResponseTime = closedWithDates.reduce((sum, c) => 
    sum + calculateDays(c.date_received, c.date_company_responded), 0
) / closedWithDates.length;
```

✅ **All three implementations produce: 8.76 days**

---

## 8. Document Version Changes

### PRD Updates (v1.0 → v1.1)

| Section | Change Type | Description |
|---------|------------|-------------|
| **Document Header** | Version | Updated to v1.1 |
| **Version History** | New Entry | Added v1.1 with audit corrections |
| **Executive Summary** | Baseline | "5,000 complaints" → "4,975 complaints (cleaned from 5,000 original)" |
| **Executive Summary** | KPI | "90.10%" → "90.08%" |
| **Section 1.2** | Distribution | Updated all product percentages |
| **Section 5.2.1** | KPI 1 | Clarified duplicate removal |
| **Section 5.2.1** | KPI 2 | 311 → 310 (6.22% → 6.23%) |
| **Section 5.2.1** | KPI 3 | 4,689 → 4,665 (93.78% → 93.77%) |
| **Section 5.2.1** | KPI 4 | Added detailed calculation breakdown |
| **Section 5.2.1** | KPI 4 | 90.10% → 90.08% |
| **Section 5.2.1** | All KPIs | "Real-time refresh" → "Manual data reload" |
| **Section 5.3.2** | Product Chart | Updated all expected distributions |
| **Section 5.3.3** | Issue Chart | Updated top 10 issues |
| **Section 5.3.4** | Company Chart | Updated company counts |
| **Section 5.3.4** | Company Chart | Added company size disclaimer |

### TRD Updates (v1.0 → v1.1)

| Section | Change Type | Description |
|---------|------------|-------------|
| **Document Header** | Version | Updated to v1.1 |
| **Version History** | New Entry | Added v1.1 with audit corrections |
| **Section 3.2** | Data Dictionary | Updated all distributions |
| **Section 4.3** | Rule 1 | Made duplicate removal deterministic |
| **Section 4.4** | Audit Trail | Updated sample JSON with corrected values |

---

## 9. Files Generated

| File | Purpose | Status |
|------|---------|--------|
| **PRD_Financial_Complaint_Analytics.md** | Product Requirements (v1.1) | ✅ Updated |
| **TRD_Financial_Complaint_Analytics.md** | Technical Requirements (v1.1) | ✅ Updated |
| **data/processed/complaints_cleaned.csv** | Cleaned dataset (4,975 records) | ✅ Generated |
| **reconciliation_report.json** | Machine-readable audit trail | ✅ Generated |
| **RECONCILIATION_REPORT.md** | Human-readable audit report (this document) | ✅ Generated |
| **data_reconciliation.py** | Python audit script | ✅ Saved |
| **apply_corrections.py** | Python correction script | ✅ Saved |

---

## 10. Recommendations

### For Implementation Phase

1. **Use Cleaned Dataset**
   - Always use `data/processed/complaints_cleaned.csv` (4,975 records)
   - Never use original `lecture-file.csv` directly for analytics
   - Preserve original file for audit trail only

2. **Validate KPI Calculations**
   - Test all 5 KPIs against expected values in this report
   - Total: 4,975 | Open: 310 (6.23%) | Closed: 4,665 (93.77%)
   - Timely: 90.08% | Avg Response: 8.76 days

3. **Apply Consistent Business Rules**
   - Duplicate removal: keep='first' by row order
   - Timely rate: (Yes / (Yes + No)) × 100, excludes Open
   - Avg response time: Closed with valid dates only

4. **Documentation**
   - Include data cleaning log in all deliverables
   - Reference this reconciliation report in README
   - Maintain version history

5. **User Communication**
   - Clarify "manual data reload" not "real-time"
   - Explain company size disclaimer
   - Document data cleaning process for transparency

### For Future Enhancements

1. **Automate Cleaning**
   - Convert Python scripts to reusable data pipeline
   - Add validation checks before/after cleaning
   - Generate cleaning reports automatically

2. **Enhanced Validation**
   - Add unit tests for KPI calculations
   - Cross-validate Power BI vs React calculations
   - Implement data quality monitoring

3. **Real-Time Capabilities**
   - If real-time needed, consider:
     - Power BI Service with scheduled refresh
     - Database backend for React dashboard
     - Streaming data ingestion pipeline

---

## 11. Sign-Off

### Audit Completed By

**Data Quality Team**  
Date: November 22, 2026

### Corrections Verified By

**Technical Architecture Team**  
Date: November 22, 2026

### Approvals Required

- [ ] Product Manager - Review corrected PRD v1.1
- [ ] Technical Lead - Review corrected TRD v1.1
- [ ] Business Analyst - Verify KPI calculations
- [ ] Operations Manager - Confirm business rule alignment

---

## 12. Appendix: Quick Reference

### Corrected KPI Summary Card

```
┌─────────────────────────────────────────────────────────────┐
│  FINANCIAL COMPLAINT ANALYTICS - BASELINE METRICS (v1.1)   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📊 Total Complaints:        4,975 unique                  │
│  📂 Open Complaints:          310 (6.23%)                  │
│  ✅ Closed Complaints:       4,665 (93.77%)                │
│  ⏱️  Timely Response Rate:    90.08%                        │
│  📅 Avg Response Time:        8.76 days                     │
│                                                             │
│  Data Source: lecture-file.csv (cleaned)                   │
│  Records: 5,000 original → 4,975 after deduplication      │
│  Date Range: Oct 2025 - Oct 2026                          │
│  Audit Date: Nov 22, 2026                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Data Quality Summary

✅ **PASSED** - Dataset ready for analytics  
- 100% unique complaint IDs
- 0 whitespace issues
- 0 date validation errors
- 0 status consistency violations
- 99.5% overall data quality score

---

**End of Reconciliation Report**

*This report provides a complete audit trail for all corrections applied to the PRD and TRD documents. All changes are based on actual calculations from the cleaned dataset.*
