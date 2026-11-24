# Power BI Desktop Dashboard Setup Guide

## Overview
This guide walks you through creating the Financial Complaint Analytics Dashboard in Power BI Desktop.

**Expected Result**: A comprehensive dashboard with KPIs, visualizations, and interactive filters matching the React dashboard functionality.

---

## Prerequisites
- Power BI Desktop installed (Download: https://powerbi.microsoft.com/desktop/)
- Cleaned data file: `data/processed/complaints_cleaned.csv`

---

## Step 1: Load Data

1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Navigate to: `d:\Projects\tekloomy\data\processed\complaints_cleaned.csv`
4. Click **Load**
5. Verify 4,975 rows loaded in the data pane

---

## Step 2: Data Model Setup

### Create Date Table (for time intelligence)
1. Go to **Modeling** tab → **New Table**
2. Enter DAX formula:
```dax
DateTable = 
CALENDAR(
    MIN(complaints_cleaned[date_received]),
    MAX(complaints_cleaned[date_received])
)
```
3. Add Month-Year column:
   - New Column → `MonthYear = FORMAT(DateTable[Date], "YYYY-MM")`
4. Create relationship:
   - **Manage Relationships** → New
   - Link: `DateTable[Date]` ↔ `complaints_cleaned[date_received]`
   - Cardinality: One-to-Many

---

## Step 3: Create DAX Measures

Navigate to **Modeling** → **New Measure** and create each:

### KPI Measures
```dax
Total Complaints = COUNTROWS(complaints_cleaned)
```

```dax
Open Complaints = 
CALCULATE(
    COUNTROWS(complaints_cleaned),
    complaints_cleaned[response_status] = "Open"
)
```

```dax
Closed Complaints = 
CALCULATE(
    COUNTROWS(complaints_cleaned),
    complaints_cleaned[response_status] = "Closed"
)
```

```dax
Timely Yes = 
CALCULATE(
    COUNTROWS(complaints_cleaned),
    complaints_cleaned[timely_response] = "Yes"
)
```

```dax
Timely No = 
CALCULATE(
    COUNTROWS(complaints_cleaned),
    complaints_cleaned[timely_response] = "No"
)
```

```dax
Timely Response Rate = 
DIVIDE(
    [Timely Yes],
    [Timely Yes] + [Timely No],
    0
) * 100
```

```dax
Avg Response Time = 
CALCULATE(
    AVERAGE(complaints_cleaned[response_time_days]),
    complaints_cleaned[response_status] = "Closed"
)
```

### Calculated Percentages
```dax
Open Rate % = 
DIVIDE([Open Complaints], [Total Complaints], 0) * 100
```

```dax
Closure Rate % = 
DIVIDE([Closed Complaints], [Total Complaints], 0) * 100
```

---

## Step 4: Build Dashboard Pages

### Page 1: Executive Summary

#### Layout Structure:
- Top: 5 KPI Cards (arranged horizontally)
- Middle: 2x2 Chart Grid
- Bottom: Full-width trend chart

#### Visuals to Add:

**1. KPI Cards (5 cards across the top)**
- Card 1: Total Complaints (Expected: 4,975)
- Card 2: Open Complaints (Expected: 310)
- Card 3: Closed Complaints (Expected: 4,665)
- Card 4: Timely Response Rate (Expected: 90.08%)
- Card 5: Avg Response Time (Expected: 8.76 days)

**2. Product Analysis (Stacked Bar Chart)**
- Visual: Stacked Bar Chart
- Axis: `financial_product`
- Values: `Open Complaints`, `Closed Complaints`
- Sort: By `Total Complaints` (descending)
- Title: "Complaints by Financial Product"

**3. Submission Channel (Pie Chart)**
- Visual: Pie Chart
- Legend: `submission_channel`
- Values: `Total Complaints`
- Data Labels: Show percentage
- Title: "Submission Channels"

**4. Top 15 States (Bar Chart)**
- Visual: Bar Chart (horizontal)
- Axis: `state`
- Values: `Total Complaints`
- Filters: Top 15 by `Total Complaints`
- Title: "Top 15 States by Complaint Volume"

**5. Response Time Distribution (Column Chart)**
- First create calculated column for buckets:
  - Go to **Data** view → `complaints_cleaned` table
  - New Column:
  ```dax
  Response Time Bucket = 
  SWITCH(
      TRUE(),
      complaints_cleaned[response_time_days] <= 3, "0-3 days",
      complaints_cleaned[response_time_days] <= 7, "4-7 days",
      complaints_cleaned[response_time_days] <= 15, "8-15 days",
      complaints_cleaned[response_time_days] <= 30, "16-30 days",
      "30+ days"
  )
  ```
- Visual: Clustered Column Chart
- Axis: `Response Time Bucket`
- Values: `Total Complaints`
- Title: "Response Time Distribution"

**6. Monthly Trends (Line Chart - Full Width)**
- Visual: Line and Clustered Column Chart
- Axis: `DateTable[MonthYear]`
- Column Values: `Total Complaints`
- Line Values: `Timely Response Rate`
- Secondary Y-axis: Enable for Timely Response Rate
- Title: "Monthly Trends (Oct 2025 - Oct 2026)"

---

### Page 2: Detailed Analysis

**1. Issue Category Table**
- Visual: Table
- Columns:
  - `issue_category`
  - `Total Complaints`
  - `Closed Complaints`
  - `Closure Rate %`
  - `Timely Response Rate`
- Sort: By `Total Complaints` (descending)
- Filters: Top 15
- Title: "Top 15 Issue Categories"

**2. Company Performance**
- Visual: Matrix
- Rows: `company_name`
- Values:
  - `Total Complaints`
  - `Timely Response Rate`
  - `Avg Response Time`
- Filters: Companies with >= 10 complaints
- Title: "Company Performance"

**3. State Heatmap (Map Visual)**
- Visual: Map
- Location: `state`
- Size: `Total Complaints`
- Title: "Geographic Distribution"

---

## Step 5: Add Slicers (Filters)

Add these slicers to allow interactive filtering:

1. **Date Range Slicer**
   - Field: `date_received`
   - Type: Between
   - Position: Top-right

2. **Financial Product Slicer**
   - Field: `financial_product`
   - Type: Dropdown
   - Position: Top-right

3. **Response Status Slicer**
   - Field: `response_status`
   - Type: Radio buttons (Open/Closed/All)
   - Position: Top-right

4. **State Slicer**
   - Field: `state`
   - Type: Dropdown
   - Position: Top-right

---

## Step 6: Format and Style

### Theme Settings:
1. **View** → **Themes** → Choose "Executive" or "Sunrise"
2. Customize colors:
   - Primary: #3b82f6 (Blue)
   - Success: #10b981 (Green)
   - Warning: #fbbf24 (Yellow)
   - Accent: #8b5cf6 (Purple)

### Title Formatting:
- Dashboard Title: 32pt, Bold
- Visual Titles: 14pt, Bold
- Font: Segoe UI

### KPI Card Formatting:
- Background: White
- Border: 1px solid #e5e7eb
- Shadow: Subtle
- Category Label: 10pt, Gray
- Data Label: 28pt, Bold, Dark Gray

---

## Step 7: Validation

**Expected KPI Values** (after all data loads):
- ✓ Total Complaints: **4,975**
- ✓ Open: **310** (6.23%)
- ✓ Closed: **4,665** (93.77%)
- ✓ Timely Response Rate: **90.08%**
- ✓ Avg Response Time: **8.76 days**

If your values don't match:
1. Check data load (should be 4,975 rows)
2. Verify DAX measures (especially division by zero handling)
3. Review filter context (ensure no accidental filters applied)

---

## Step 8: Save and Publish

1. **File** → **Save As** → Name: `Financial_Complaint_Analytics.pbix`
2. Save to: `d:\Projects\tekloomy\powerbi\`
3. (Optional) **Publish** to Power BI Service for online sharing

---

## Additional Resources

- **SQL Query Results**: Reference `sql/results/` for data validation
- **React Dashboard**: Compare with `react-dashboard/` for visual consistency
- **Power BI Documentation**: https://docs.microsoft.com/power-bi/

---

## Troubleshooting

### Issue: KPIs don't match expected values
**Solution**: 
- Verify CSV loaded correctly (4,975 rows)
- Check for hidden filters on the page
- Review DAX measure formulas

### Issue: Date intelligence not working
**Solution**:
- Ensure DateTable relationship is active
- Mark DateTable as Date Table (Right-click → Mark as Date Table)

### Issue: Charts show "Blank" category
**Solution**:
- Data quality: Some states are missing (49 records)
- This is expected - you can filter blanks out or keep for transparency

---

## Next Steps

After completing the Power BI dashboard:
1. Compare visualizations with React dashboard
2. Test interactive filters and drill-downs
3. Export to PDF for stakeholder review
4. Document any insights discovered

---

**Setup Time Estimate**: 30-45 minutes for experienced users

**Difficulty**: Intermediate (requires basic Power BI knowledge)
