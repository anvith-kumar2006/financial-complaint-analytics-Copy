# Product Requirements Document (PRD)
## Financial Customer Complaint Analytics Platform

---

## Document Information

| Property | Value |
|----------|-------|
| **Document Title** | Product Requirements Document - Financial Customer Complaint Analytics Platform |
| **Version** | 1.1 |
| **Date** | November 22, 2026 |
| **Author** | Product Management Team |
| **Status** | Draft |
| **Classification** | Internal |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-11-22 | Product Team | Initial PRD based on actual dataset analysis |
| 1.1 | 2026-11-22 | Product Team | Corrected KPI baselines after data cleaning audit, updated all distributions to cleaned data values, fixed real-time refresh claims |

---

## Executive Summary

The Financial Customer Complaint Analytics Platform is a comprehensive business intelligence solution designed to transform raw customer complaint data into actionable insights for operations managers, customer experience analysts, and business leadership. 

The platform addresses the critical business need for complaint monitoring (with manual data refresh), trend analysis, and response performance measurement across financial products and services. With 4,975 customer complaints (cleaned from 5,000 original records) spanning 8 financial service companies and covering the period from October 2025 to October 2026, this platform will enable data-driven decision-making to improve customer satisfaction and operational efficiency.

The solution consists of two complementary dashboards:
1. **Power BI Desktop Dashboard** (Mandatory) - Enterprise-grade analytics with interactive visualizations
2. **React Web Dashboard** (Additional) - Modern, responsive web application for broader accessibility

**Key Business Impact:**
- Reduce average complaint response time (current: 8.76 days)
- Maintain high timely response rate (current: 90.08%)
- Identify high-volume complaint categories for proactive intervention
- Enable product-specific and company-specific performance benchmarking

---

## 1. Product Vision

### 1.1 Vision Statement

To empower financial service organizations with transparent, actionable complaint analytics that drive continuous improvement in customer experience and operational excellence.

### 1.2 Business Background

Financial service organizations face mounting regulatory pressure and customer expectations around complaint handling. The organization receives complaints across multiple financial products:

- **Credit Cards** (23.80% of complaints)
- **Checking or Savings Accounts** (21.08%)
- **Credit Reporting** (18.12%)
- **Personal Loans** (16.46%)
- **Mortgages** (12.96%)
- **Buy Now, Pay Later** (7.06%)

Current challenges include:
- Lack of timely visibility into complaint volumes and trends
- Inconsistent data quality (25 duplicate complaint IDs, 49 missing state values, whitespace issues in product categories)
- Limited ability to benchmark response performance across companies
- Manual, time-consuming complaint analysis processes
- Difficulty identifying systemic product or service issues

### 1.3 Problem Statement

**Current State:**
Operations managers and customer experience teams lack a unified, interactive platform to monitor and analyze customer complaint patterns. Data exists in raw CSV format requiring manual analysis, leading to delayed insights and reactive (rather than proactive) problem resolution.

**Desired State:**
Automated complaint analytics (with manual data reload) accessible through intuitive dashboards, enabling stakeholders to quickly identify trends, measure response performance, and take corrective action.

**Business Impact:**
- Improved regulatory compliance through better response time monitoring
- Enhanced customer satisfaction through proactive issue resolution
- Operational cost reduction through process optimization
- Data-driven resource allocation based on complaint volume patterns

---

## 2. Business Objectives

### 2.1 Primary Objectives

| Objective | Success Metric | Target |
|-----------|---------------|--------|
| **Complaint Visibility** | Time to identify emerging complaint trends | < 1 day (from 7+ days manual) |
| **Response Performance** | Timely response rate | Maintain ≥ 90% (current: 90.08%) |
| **Data Quality** | Clean, standardized complaint records | 100% data validation |
| **User Adoption** | Active dashboard users (operations + analysts) | 100% of target user base |
| **Decision Speed** | Time from insight to action | 50% reduction |

### 2.2 Secondary Objectives

- Enable self-service analytics for business analysts
- Reduce manual reporting effort by 80%
- Establish baseline metrics for year-over-year complaint trend comparison
- Support regulatory audit requirements with comprehensive complaint documentation

---

## 3. Stakeholder Analysis

### 3.1 Primary Stakeholders

| Stakeholder Group | Role | Key Interests | Success Criteria |
|------------------|------|---------------|------------------|
| **Operations Managers** | Primary User | Real-time complaint monitoring, resource planning | Quick access to complaint volumes and trends |
| **Customer Experience Analysts** | Primary User | Identify root causes, measure satisfaction | Drill-down capability by product/issue |
| **Business Analysts** | Primary User | Historical trend analysis, forecasting | Export capability, flexible filtering |
| **Executive Leadership** | Consumer | High-level KPIs, strategic insights | Clear KPI cards, executive summary views |

### 3.2 Secondary Stakeholders

| Stakeholder Group | Role | Key Interests |
|------------------|------|---------------|
| **Compliance Team** | Consumer | Regulatory adherence monitoring |
| **IT/Data Engineering** | Supporter | Data pipeline maintenance, system performance |
| **Customer Service Teams** | Indirect Beneficiary | Actionable feedback for service improvement |

---

## 4. Target Users and Personas

### 4.1 Persona 1: Sarah - Operations Manager

**Background:**
- 8+ years in financial services operations
- Manages a team of 15 customer service representatives
- Responsible for meeting SLA targets and compliance requirements

**Goals:**
- Monitor daily complaint volumes to allocate staff effectively
- Track timely response rates to ensure SLA compliance
- Identify patterns requiring process improvements

**Pain Points:**
- Currently relies on manual Excel analysis (2-3 hours daily)
- Discovers complaint spikes days after they occur
- Difficult to compare performance across companies/products

**Primary Use Cases:**
- Morning dashboard review to identify overnight complaint trends
- Weekly team meetings with KPI performance data
- Month-end reporting to leadership

---

### 4.2 Persona 2: Michael - Customer Experience Analyst

**Background:**
- 5 years in customer analytics
- Data-driven approach to identifying service improvement opportunities
- Works closely with product teams

**Goals:**
- Identify root causes of complaint spikes
- Analyze complaint patterns by product and issue category
- Provide actionable recommendations to product teams

**Pain Points:**
- Limited ability to drill down into specific issue categories
- Time-consuming data preparation before analysis
- Lack of historical trend visibility

**Primary Use Cases:**
- Root cause analysis for complaint spikes
- Product-specific complaint deep dives
- Quarterly trend reporting with year-over-year comparisons

---

### 4.3 Persona 3: Jennifer - Business Intelligence Analyst

**Background:**
- 6 years in business intelligence and reporting
- Supports multiple business units with data analysis
- Advanced Excel and BI tool expertise

**Goals:**
- Create ad-hoc reports for stakeholders
- Perform trend analysis and forecasting
- Maintain data quality and consistency

**Pain Points:**
- Data quality issues (duplicates, missing values, formatting inconsistencies)
- Manual data cleaning before every analysis
- Limited visualization capabilities in current tools

**Primary Use Cases:**
- Ad-hoc analysis requests from leadership
- Data quality monitoring and validation
- Custom report creation for specific business questions

---

## 5. Functional Requirements

### 5.1 Data Management Requirements

#### 5.1.1 Data Ingestion (Must Have)

**Requirement ID:** FR-DM-001  
**Priority:** Must Have  
**Description:** System must ingest complaint data from CSV files

**Acceptance Criteria:**
- Support CSV file format with 14 columns as specified in data dictionary
- Handle files up to 10,000 records
- Validate file structure before import
- Provide import success/failure confirmation

---

#### 5.1.2 Data Cleaning and Standardization (Must Have)

**Requirement ID:** FR-DM-002  
**Priority:** Must Have  
**Description:** System must clean and standardize complaint data

**Acceptance Criteria:**
- **Duplicate Handling:**
  - Identify duplicate complaint IDs (25 duplicates in current dataset)
  - Flag or remove duplicates based on business rules
  - Log all duplicate detection actions
  
- **Missing Value Handling:**
  - Handle 49 missing state values (0.98%)
  - Handle 310 missing response dates and timely response flags (Open complaints)
  - Preserve missing data as NULL/Unknown, never fabricate values
  
- **Financial Product Standardization:**
  - Remove leading/trailing whitespace (affects 26 records)
  - Standardize casing to title case
  - Map variants to standard categories:
    - " credit card " → "Credit card"
    - " checking or savings account " → "Checking or savings account"
    - " personal loan " → "Personal loan"
    - " mortgage " → "Mortgage"
    - " credit reporting " → "Credit reporting"
  
- **Date Validation:**
  - Validate date_received format (YYYY-MM-DD)
  - Validate date_company_responded format
  - Ensure response date ≥ received date
  - Flag invalid dates for review
  
- **Status Consistency Validation:**
  - Open complaints must not have response dates or timely response flags
  - Closed complaints must have response dates
  - Log all consistency check failures

**Data Quality Audit Trail:**
- Before-and-after record counts
- Detailed cleaning log with timestamp
- Summary report of all corrections applied

---

#### 5.1.3 Data Storage (Must Have)

**Requirement ID:** FR-DM-003  
**Priority:** Must Have  
**Description:** System must maintain original and cleaned datasets

**Acceptance Criteria:**
- Preserve original CSV file in `data/original/` directory
- Store cleaned dataset in `data/processed/` directory
- Never modify or overwrite original dataset
- Support incremental data loads for future updates

---

### 5.2 Business Metrics and KPI Requirements

#### 5.2.1 Core KPI Definitions (Must Have)

**Requirement ID:** FR-BM-001  
**Priority:** Must Have  
**Description:** System must calculate and display five core KPIs

**KPI Specifications:**

1. **Total Complaints**
   - **Definition:** Count of unique complaint IDs
   - **Current Baseline:** 4,975 unique complaints (after removing 25 duplicates from 5,000 original records)
   - **Refresh:** Manual data reload required (static CSV architecture)
   - **Display Format:** Integer with thousand separator (e.g., "4,975")

2. **Open Complaints**
   - **Definition:** Count of complaints with response_status = "Open"
   - **Current Baseline:** 310 (6.23% of total)
   - **Refresh:** Manual data reload required (static CSV architecture)
   - **Display Format:** Integer with percentage of total (e.g., "310 (6.23%)")

3. **Closed Complaints**
   - **Definition:** Count of complaints with response_status = "Closed"
   - **Current Baseline:** 4,665 (93.77% of total)
   - **Refresh:** Manual data reload required (static CSV architecture)
   - **Display Format:** Integer with percentage of total (e.g., "4,665 (93.77%)")

4. **Timely Response Rate**
   - **Definition:** (Timely Yes / (Timely Yes + Timely No)) × 100
   - **Scope:** Closed complaints only
   - **Current Baseline:** 90.08% (4,202 Yes / 4,665 total = 4,202 Yes + 463 No)
   - **Refresh:** Manual data reload required (static CSV architecture)
   - **Display Format:** Percentage with 2 decimal places (e.g., "90.08%")
   - **Business Rules:**
     - Exclude open complaints from calculation
     - Exclude complaints with missing timely_response values
     - Display "N/A" if no closed complaints with timely response data
   - **Calculation Details:**
     - Numerator: Closed complaints with timely_response = "Yes" (4,202)
     - Denominator: Closed complaints with timely_response = "Yes" OR "No" (4,665)
     - Excludes: Open complaints AND Closed complaints without timely response flag
     - Formula: (4,202 / 4,665) × 100 = 90.08%

5. **Average Response Time**
   - **Definition:** Average of (date_company_responded - date_received) in days
   - **Scope:** Closed complaints with valid dates only
   - **Current Baseline:** 8.76 days (range: 1-25 days, median: 8 days)
   - **Refresh:** Manual data reload required (static CSV architecture)
   - **Display Format:** Decimal with 2 places + "days" label (e.g., "8.76 days")
   - **Business Rules:**
     - Exclude open complaints
     - Exclude complaints with missing response dates
     - Display "N/A" if no valid closed complaints

**Important Business Rules:**
- Higher complaint counts do not automatically indicate poor company performance (company sizes differ)
- Timely responses do not necessarily indicate customer satisfaction
- All data is fictional and for analytical training purposes

---

### 5.3 Visualization Requirements

#### 5.3.1 Monthly Complaint Trends Chart (Must Have)

**Requirement ID:** FR-VIZ-001  
**Priority:** Must Have  
**Description:** Line chart showing complaint volume over time

**Acceptance Criteria:**
- **Chart Type:** Line chart
- **X-Axis:** Month (Oct 2025 - Oct 2026)
- **Y-Axis:** Total complaint count
- **Data Points:** Monthly aggregation of complaints by date_received
- **Interactivity:** 
  - Hover to show exact count
  - Click to filter other visualizations (Power BI only)
- **Date Range:** Covers October 2025 to October 2026 (13 months)

---

#### 5.3.2 Complaints by Financial Product Chart (Must Have)

**Requirement ID:** FR-VIZ-002  
**Priority:** Must Have  
**Description:** Bar chart showing complaint distribution across products

**Acceptance Criteria:**
- **Chart Type:** Horizontal bar chart
- **X-Axis:** Complaint count
- **Y-Axis:** Financial product categories (6 standardized categories)
- **Sorting:** Descending by complaint count
- **Data Labels:** Show count and percentage
- **Expected Distribution (Cleaned Data):**
  - Credit card: 1,191 (23.94%)
  - Checking or savings account: 1,054 (21.19%)
  - Credit reporting: 906 (18.21%)
  - Personal loan: 826 (16.60%)
  - Mortgage: 648 (13.03%)
  - Buy now, pay later: 350 (7.04%)
- **Color Coding:** Distinct color per product category

---

#### 5.3.3 Most Frequently Reported Issues Chart (Must Have)

**Requirement ID:** FR-VIZ-003  
**Priority:** Must Have  
**Description:** Bar chart showing top complaint issue categories

**Acceptance Criteria:**
- **Chart Type:** Horizontal bar chart
- **X-Axis:** Complaint count
- **Y-Axis:** Issue category
- **Display:** Top 10 issue categories
- **Sorting:** Descending by complaint count
- **Data Labels:** Show count
- **Expected Top Issues:**
  1. Unexpected fees: 545
  2. Account access: 337
  3. Fraudulent charges: 307
  4. Card declined: 299
  5. Billing dispute: 296
  6. Transaction dispute: 285
  7. Account closure: 259
  8. Report access: 242
  9. Incorrect information: 228
  10. Loan servicing: 226

---

#### 5.3.4 Timely Response Performance by Company Chart (Must Have)

**Requirement ID:** FR-VIZ-004  
**Priority:** Must Have  
**Description:** Column/bar chart showing timely response rate by company

**Acceptance Criteria:**
- **Chart Type:** Clustered column or bar chart
- **X-Axis:** Company name (8 companies)
- **Y-Axis:** Timely response percentage (0-100%)
- **Calculation:** (Timely Yes / (Timely Yes + Timely No)) × 100 per company
- **Reference Line:** 90% target line
- **Data Labels:** Show percentage
- **Sorting:** Descending by timely response rate
- **Expected Companies:**
  - Harbor Credit: 669 complaints
  - Silverline Lending: 637 complaints
  - Atlas Consumer Finance: 630 complaints
  - Northstar Financial: 628 complaints
  - OakBridge Services: 629 complaints
  - BluePeak Bank: 618 complaints
  - Cedar Finance: 602 complaints
  - Summit Payments: 562 complaints
- **Color Coding:**
  - Green: ≥ 90% timely response
  - Yellow: 80-89% timely response
  - Red: < 80% timely response
- **Important Disclaimer:**
  - Higher complaint volumes do not necessarily indicate poor company performance
  - Company sizes differ significantly
  - Compare timely response rates, not absolute complaint counts
  - Use this chart for relative performance benchmarking only

---

### 5.4 Interactive Filtering Requirements

#### 5.4.1 Date Range Filter (Must Have)

**Requirement ID:** FR-FILT-001  
**Priority:** Must Have  
**Description:** Date range selector for temporal analysis

**Acceptance Criteria:**
- **Filter Type:** Date range picker or slider
- **Date Field:** date_received
- **Default Range:** Full dataset (Oct 2025 - Oct 2026)
- **Minimum Range:** 1 day
- **Maximum Range:** All available data
- **Behavior:** Applies to all visualizations and KPIs
- **User Experience:**
  - Visual feedback showing selected range
  - Quick select options: Last 30 days, Last 90 days, Year to date, All time
  - Manual start/end date entry

---

#### 5.4.2 Company Filter (Must Have)

**Requirement ID:** FR-FILT-002  
**Priority:** Must Have  
**Description:** Multi-select company filter

**Acceptance Criteria:**
- **Filter Type:** Multi-select dropdown or checkbox list
- **Options:** All 8 companies
- **Default State:** All companies selected
- **Behavior:** Applies to all visualizations and KPIs
- **User Experience:**
  - Select all / Deselect all options
  - Search/filter company names
  - Show complaint count next to company name

---

#### 5.4.3 Financial Product Filter (Must Have)

**Requirement ID:** FR-FILT-003  
**Priority:** Must Have  
**Description:** Multi-select financial product filter

**Acceptance Criteria:**
- **Filter Type:** Multi-select dropdown or checkbox list
- **Options:** 6 standardized product categories
- **Default State:** All products selected
- **Behavior:** Applies to all visualizations and KPIs
- **User Experience:**
  - Select all / Deselect all options
  - Show complaint count next to product name
  - Color-coded to match product chart

---

#### 5.4.4 Filter Interaction and Synchronization (Must Have)

**Requirement ID:** FR-FILT-004  
**Priority:** Must Have  
**Description:** Filters must work together and update all dashboard elements

**Acceptance Criteria:**
- All three filters (date, company, product) work together (AND logic)
- Changing any filter immediately updates:
  - All 5 KPI cards
  - All 4 visualizations
  - All other filters (show available options based on current selection)
- Display "No data available" message when filters result in empty dataset
- "Clear all filters" button resets to default state
- Visual loading indicator during filter application
- Filter state persists within session (Power BI) or browser session (React)

---

### 5.5 Power BI Specific Requirements

#### 5.5.1 Power BI Desktop Report (Must Have)

**Requirement ID:** FR-PBI-001  
**Priority:** Must Have  
**Description:** Deliverable Power BI Desktop .pbix file

**Acceptance Criteria:**
- **File Format:** .pbix (Power BI Desktop file)
- **Power BI Version:** Compatible with Power BI Desktop (latest stable version as of Nov 2026)
- **Data Source:** Cleaned CSV file from data/processed/ directory
- **Report Pages:**
  - Page 1: Executive Dashboard (KPIs + all 4 visualizations + filters)
  - Optional Page 2: Detailed complaint list (table view)
- **File Location:** `powerbi/Financial_Complaint_Analytics.pbix`
- **File Size:** Optimized (< 50MB)

---

#### 5.5.2 Power BI Data Model (Must Have)

**Requirement ID:** FR-PBI-002  
**Priority:** Must Have  
**Description:** Properly structured data model with relationships

**Acceptance Criteria:**
- **Tables:**
  - Fact table: Complaints (main data)
  - Dimension table: Date (date_received calendar)
  - Optional dimension tables: Companies, Products, States
- **Relationships:**
  - One-to-many from Date to Complaints
  - Proper filter direction configuration
- **Data Types:**
  - Dates properly formatted as Date type
  - Numeric fields (response time calculations) as integers/decimals
  - Text fields as Text type
- **Column Organization:**
  - Hide technical columns not needed for reporting
  - Organize columns into logical display folders

---

#### 5.5.3 DAX Measures (Must Have)

**Requirement ID:** FR-PBI-003  
**Priority:** Must Have  
**Description:** DAX measures for all KPIs and calculations

**Required Measures:**

```dax
-- Total Complaints
Total Complaints = DISTINCTCOUNT(Complaints[complaint_id])

-- Open Complaints
Open Complaints = CALCULATE(
    DISTINCTCOUNT(Complaints[complaint_id]),
    Complaints[response_status] = "Open"
)

-- Closed Complaints
Closed Complaints = CALCULATE(
    DISTINCTCOUNT(Complaints[complaint_id]),
    Complaints[response_status] = "Closed"
)

-- Timely Response Rate
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

-- Average Response Time
Average Response Time = 
CALCULATE(
    AVERAGE(Complaints[response_time_days]),
    Complaints[response_status] = "Closed",
    NOT(ISBLANK(Complaints[response_time_days]))
)

-- Where response_time_days is a calculated column:
-- response_time_days = DATEDIFF(Complaints[date_received], Complaints[date_company_responded], DAY)
```

**Acceptance Criteria:**
- All 5 KPI measures created and tested
- Measures organized in dedicated "Measures" folder
- Proper formatting (%, days, commas) applied
- Measures handle blank/missing values gracefully
- Measures properly respond to all filters

---

#### 5.5.4 Power BI Report Formatting (Should Have)

**Requirement ID:** FR-PBI-004  
**Priority:** Should Have  
**Description:** Professional, consistent formatting and branding

**Acceptance Criteria:**
- **Theme:** Professional business theme (Blues/Grays recommended)
- **Layout:** Logical flow - KPIs at top, charts below, filters on left sidebar
- **Typography:** Clear, readable fonts (Segoe UI or similar)
- **Color Scheme:**
  - Consistent colors across all visualizations
  - Accessible color choices (colorblind-friendly)
- **KPI Cards:**
  - Large, prominent numbers
  - Clear labels
  - Subtle icons or background colors
  - Trend indicators (if comparing periods)
- **Responsive Design:** Adapts to different screen sizes
- **Whitespace:** Appropriate spacing between elements

---

### 5.6 React Web Dashboard Requirements

#### 5.6.1 Technology Stack (Must Have)

**Requirement ID:** FR-REACT-001  
**Priority:** Must Have  
**Description:** Modern React application with specified technology stack

**Technology Requirements:**
- **Framework:** React 18+
- **Language:** TypeScript (strict mode)
- **Build Tool:** Vite
- **Styling:** Tailwind CSS 3+
- **Charts:** Recharts library
- **Deployment:** Vercel
- **Version Control:** GitHub

**Acceptance Criteria:**
- Project initialized with Vite + React + TypeScript template
- Tailwind CSS properly configured
- Recharts installed and configured
- TypeScript strict mode enabled
- ESLint and Prettier configured
- Git repository initialized

---

#### 5.6.2 React Component Structure (Must Have)

**Requirement ID:** FR-REACT-002  
**Priority:** Must Have  
**Description:** Well-organized, modular component architecture

**Component Specifications:**

```
src/
├── components/
│   ├── KPICard.tsx          // Reusable KPI display card
│   ├── MonthlyTrendChart.tsx    // Line chart component
│   ├── ProductChart.tsx         // Product bar chart
│   ├── IssueChart.tsx          // Issue bar chart
│   ├── CompanyPerformanceChart.tsx  // Company performance chart
│   ├── DateFilter.tsx          // Date range filter
│   ├── CompanyFilter.tsx       // Company multi-select
│   ├── ProductFilter.tsx       // Product multi-select
│   ├── LoadingState.tsx        // Loading spinner
│   ├── EmptyState.tsx          // No data message
│   └── ErrorState.tsx          // Error display
├── hooks/
│   ├── useComplaintData.ts     // Data loading and filtering
│   └── useFilters.ts           // Filter state management
├── types/
│   └── complaint.ts            // TypeScript interfaces
├── utils/
│   ├── dataProcessing.ts       // Data cleaning logic
│   └── calculations.ts         // KPI calculation functions
├── data/
│   └── complaints.csv          // Data file
├── App.tsx                     // Main application
└── main.tsx                    // Entry point
```

**Acceptance Criteria:**
- All components properly typed with TypeScript
- Components are reusable and single-responsibility
- Proper props interfaces defined
- No prop drilling (use Context or props appropriately)

---

#### 5.6.3 React Dashboard Features (Must Have)

**Requirement ID:** FR-REACT-003  
**Priority:** Must Have  
**Description:** Feature parity with Power BI dashboard

**Acceptance Criteria:**
- **KPI Cards (5):** Display all 5 KPIs with proper formatting
- **Monthly Trend Chart:** Line chart with Recharts
- **Product Chart:** Bar chart with Recharts
- **Issue Chart:** Bar chart with Recharts (top 10)
- **Company Performance Chart:** Bar chart with Recharts
- **Date Filter:** Functional date range selector
- **Company Filter:** Multi-select with checkboxes
- **Product Filter:** Multi-select with checkboxes
- **Filter Synchronization:** All filters update all visualizations
- **Responsive Design:** Works on desktop (1920px), tablet (768px), mobile (375px)
- **Loading States:** Spinner during data loading
- **Empty States:** Clear message when no data matches filters
- **Error Handling:** User-friendly error messages

---

#### 5.6.4 React Data Processing (Must Have)

**Requirement ID:** FR-REACT-004  
**Priority:** Must Have  
**Description:** Client-side data cleaning and processing

**Acceptance Criteria:**
- Load CSV data at application startup
- Apply all data cleaning rules (same as FR-DM-002)
- Calculate derived fields (response_time_days)
- Implement all KPI calculations (same logic as DAX measures)
- Filter data based on user selections
- Optimize for performance (memoization, lazy loading)

---

#### 5.6.5 React UI/UX Requirements (Should Have)

**Requirement ID:** FR-REACT-005  
**Priority:** Should Have  
**Description:** Professional, financial analytics UI design

**Acceptance Criteria:**
- **Color Scheme:** Professional blues/grays matching financial industry standards
- **Typography:** Clear hierarchy, readable fonts
- **Spacing:** Consistent padding/margins using Tailwind
- **Animations:** Subtle transitions (chart updates, filter changes)
- **Accessibility:**
  - ARIA labels on interactive elements
  - Keyboard navigation support
  - Minimum contrast ratios (WCAG AA)
  - Screen reader compatibility
- **Responsive Breakpoints:**
  - Desktop: 1024px+
  - Tablet: 768px - 1023px
  - Mobile: < 768px

---

#### 5.6.6 Vercel Deployment (Must Have)

**Requirement ID:** FR-REACT-006  
**Priority:** Must Have  
**Description:** Deploy React application to Vercel

**Acceptance Criteria:**
- GitHub repository connected to Vercel
- Automatic deployment on push to main branch
- Production URL accessible publicly
- Environment variables configured (if needed)
- Build succeeds without errors
- Application loads and functions correctly in production

---

### 5.7 Data Validation and Quality Requirements

#### 5.7.1 Data Validation Rules (Must Have)

**Requirement ID:** FR-VAL-001  
**Priority:** Must Have  
**Description:** Validate data integrity before visualization

**Validation Rules:**

1. **Complaint ID Validation:**
   - Must not be empty
   - Must follow pattern "CMP-XXXXXX"
   - Must be unique (flag duplicates)

2. **Date Validation:**
   - date_received must be valid date
   - date_company_responded must be valid date (if closed)
   - response_due_date must be valid date
   - date_company_responded must be ≥ date_received
   - Dates must be within reasonable range (2025-2026)

3. **Status Validation:**
   - response_status must be "Open" or "Closed"
   - If Open: date_company_responded and timely_response must be empty
   - If Closed: date_company_responded must not be empty

4. **Timely Response Validation:**
   - Must be "Yes", "No", or empty
   - Should only be populated for Closed complaints

5. **Financial Product Validation:**
   - Must be one of 6 standardized categories (after cleaning)
   - No extra whitespace

6. **Company Name Validation:**
   - Must be one of 8 known companies
   - Consistent spelling

**Acceptance Criteria:**
- All validation rules implemented
- Validation errors logged with detail
- Option to exclude invalid records or flag for review
- Validation summary report available

---

### 5.8 Export and Reporting Requirements (Should Have)

#### 5.8.1 Data Export Capability (Should Have)

**Requirement ID:** FR-EXP-001  
**Priority:** Should Have  
**Description:** Allow users to export filtered data

**Acceptance Criteria:**
- **Power BI:** Export to Excel functionality
- **React Dashboard:** Export to CSV button
- Export respects current filter selections
- Export includes:
  - All visible complaint records
  - Current KPI values (summary sheet)
- Export filename includes timestamp
- Max export size: 10,000 records

---

## 6. Non-Functional Requirements

### 6.1 Performance Requirements

**Requirement ID:** NFR-PERF-001  
**Priority:** Must Have  

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Dashboard Load Time** | < 3 seconds | Time to interactive state |
| **Filter Response Time** | < 1 second | Time to update all visualizations |
| **Data Refresh** | < 5 seconds | Time to reload data file |
| **Concurrent Users** | 50+ | Power BI Desktop / Vercel hosting |

---

### 6.2 Usability Requirements

**Requirement ID:** NFR-USAB-001  
**Priority:** Must Have  

- **Learning Curve:** New users productive within 15 minutes
- **Navigation:** Intuitive, self-explanatory interface
- **Help Documentation:** Inline tooltips, user guide
- **Error Messages:** Clear, actionable error messages
- **Accessibility:** WCAG 2.1 AA compliance (for React dashboard)

---

### 6.3 Compatibility Requirements

**Requirement ID:** NFR-COMP-001  
**Priority:** Must Have  

**Power BI:**
- Windows 10/11
- Power BI Desktop (latest stable version)
- Minimum 4GB RAM, 8GB recommended

**React Dashboard:**
- Browsers: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- Devices: Desktop, tablet, mobile
- Screen resolutions: 375px to 2560px

---

### 6.4 Data Security and Privacy Requirements

**Requirement ID:** NFR-SEC-001  
**Priority:** Must Have  

- **Data Classification:** All complaint data is fictional (training data)
- **Access Control:** Dashboard access controlled by deployment method (file sharing for Power BI, URL access for React)
- **Data Transmission:** HTTPS for React dashboard
- **No PII:** Dataset contains no personally identifiable customer information
- **Audit Trail:** Data cleaning operations logged

---

### 6.5 Maintainability Requirements

**Requirement ID:** NFR-MAINT-001  
**Priority:** Should Have  

- **Code Documentation:** Inline comments, README files
- **Version Control:** Git with meaningful commit messages
- **Code Style:** Consistent formatting (ESLint for React)
- **Modularity:** Reusable components and functions
- **Update Process:** Clear instructions for data updates

---

## 7. User Stories and Acceptance Criteria

### 7.1 Epic 1: Dashboard Monitoring

#### User Story 1.1: View Complaint Volume KPIs

**As an** Operations Manager  
**I want to** see total, open, and closed complaint counts at a glance  
**So that** I can quickly assess current workload

**Acceptance Criteria:**
- [ ] Dashboard displays 3 KPI cards: Total, Open, Closed complaints
- [ ] Numbers update based on filter selections
- [ ] Open complaints show percentage of total
- [ ] Closed complaints show percentage of total
- [ ] Visual distinction between Open and Closed (color coding)

**Priority:** Must Have  
**Story Points:** 3

---

#### User Story 1.2: Monitor Response Performance

**As an** Operations Manager  
**I want to** see timely response rate and average response time  
**So that** I can ensure we meet SLA targets

**Acceptance Criteria:**
- [ ] Dashboard displays 2 KPI cards: Timely Response Rate, Average Response Time
- [ ] Timely response rate shown as percentage
- [ ] Average response time shown in days
- [ ] Visual indicator when timely response rate < 90% (warning state)
- [ ] KPIs exclude open complaints from calculations

**Priority:** Must Have  
**Story Points:** 5

---

### 7.2 Epic 2: Trend Analysis

#### User Story 2.1: Analyze Monthly Complaint Trends

**As a** Customer Experience Analyst  
**I want to** see complaint volumes over time  
**So that** I can identify seasonal patterns and unusual spikes

**Acceptance Criteria:**
- [ ] Line chart displays complaints by month
- [ ] Chart covers full date range (Oct 2025 - Oct 2026)
- [ ] Hover shows exact complaint count for each month
- [ ] Chart updates when filters are applied
- [ ] Clear axis labels and title

**Priority:** Must Have  
**Story Points:** 5

---

#### User Story 2.2: Compare Product Complaint Volumes

**As a** Customer Experience Analyst  
**I want to** see which financial products generate the most complaints  
**So that** I can prioritize improvement efforts

**Acceptance Criteria:**
- [ ] Bar chart displays complaints by product category
- [ ] Chart shows all 6 product categories
- [ ] Products sorted by complaint count (descending)
- [ ] Data labels show count and percentage
- [ ] Distinct colors for each product

**Priority:** Must Have  
**Story Points:** 3

---

### 7.3 Epic 3: Issue Identification

#### User Story 3.1: Identify Top Complaint Issues

**As a** Business Analyst  
**I want to** see the most frequently reported issues  
**So that** I can identify systemic problems

**Acceptance Criteria:**
- [ ] Bar chart displays top 10 issue categories
- [ ] Issues sorted by complaint count (descending)
- [ ] Data labels show exact count
- [ ] Chart updates based on product/company filters
- [ ] Clear axis labels

**Priority:** Must Have  
**Story Points:** 3

---

### 7.4 Epic 4: Company Performance

#### User Story 4.1: Compare Company Response Performance

**As an** Operations Manager  
**I want to** see timely response rates by company  
**So that** I can benchmark performance and identify best practices

**Acceptance Criteria:**
- [ ] Bar chart displays timely response rate by company
- [ ] Chart shows all 8 companies
- [ ] Companies sorted by timely response rate (descending)
- [ ] Reference line at 90% target
- [ ] Color coding: Green (≥90%), Yellow (80-89%), Red (<80%)
- [ ] Data labels show percentage

**Priority:** Must Have  
**Story Points:** 5

---

### 7.5 Epic 5: Data Filtering

#### User Story 5.1: Filter by Date Range

**As a** Business Analyst  
**I want to** filter complaints by date range  
**So that** I can analyze specific time periods

**Acceptance Criteria:**
- [ ] Date range picker available on dashboard
- [ ] Quick select options: Last 30 days, Last 90 days, YTD, All time
- [ ] Custom start and end date entry
- [ ] All KPIs and charts update when date filter changes
- [ ] Visual feedback showing selected date range

**Priority:** Must Have  
**Story Points:** 5

---

#### User Story 5.2: Filter by Company

**As an** Operations Manager  
**I want to** filter complaints by one or more companies  
**So that** I can analyze company-specific performance

**Acceptance Criteria:**
- [ ] Multi-select company filter available
- [ ] All 8 companies shown with complaint counts
- [ ] Select all / Deselect all functionality
- [ ] All KPIs and charts update when company filter changes
- [ ] Selected companies visually indicated

**Priority:** Must Have  
**Story Points:** 3

---

#### User Story 5.3: Filter by Financial Product

**As a** Customer Experience Analyst  
**I want to** filter complaints by product category  
**So that** I can conduct product-specific analysis

**Acceptance Criteria:**
- [ ] Multi-select product filter available
- [ ] All 6 products shown with complaint counts
- [ ] Select all / Deselect all functionality
- [ ] All KPIs and charts update when product filter changes
- [ ] Color-coded to match product chart

**Priority:** Must Have  
**Story Points:** 3

---

#### User Story 5.4: Reset Filters

**As a** dashboard user  
**I want to** easily reset all filters to default  
**So that** I can quickly return to the full dataset view

**Acceptance Criteria:**
- [ ] "Clear all filters" or "Reset" button visible
- [ ] Button resets date, company, and product filters to defaults
- [ ] All visualizations return to full dataset view
- [ ] Visual feedback confirming filter reset

**Priority:** Should Have  
**Story Points:** 2

---

### 7.6 Epic 6: Data Quality

#### User Story 6.1: View Clean, Standardized Data

**As a** Business Analyst  
**I want to** work with clean, standardized complaint data  
**So that** my analysis is accurate and reliable

**Acceptance Criteria:**
- [ ] Duplicate complaint IDs removed
- [ ] Financial product names standardized (no whitespace)
- [ ] Missing state values preserved as NULL (not fabricated)
- [ ] Date fields properly formatted
- [ ] Status consistency validated (Open complaints have no response dates)
- [ ] Data cleaning log available for review

**Priority:** Must Have  
**Story Points:** 8

---

## 8. Out of Scope

The following features are explicitly **out of scope** for the initial release:

### 8.1 Not Included in Initial Release

- **Predictive Analytics:** Forecasting future complaint volumes
- **Sentiment Analysis:** Natural language processing of complaint summaries
- **Real-Time Data Streaming:** Live data ingestion from complaint systems
- **Multi-Language Support:** Dashboard localization
- **Mobile Native Apps:** iOS/Android applications (responsive web only)
- **Advanced User Management:** Role-based access control, user authentication
- **Integration with CRM Systems:** Salesforce, Zendesk, etc.
- **Automated Alerting:** Email/SMS notifications for complaint spikes
- **Customer-Facing Portal:** External customer complaint tracking
- **API Development:** RESTful API for external data access
- **Data Warehouse Integration:** Enterprise data warehouse connectivity
- **Advanced Statistical Analysis:** Regression, correlation, significance testing
- **Custom Report Builder:** User-created custom reports beyond provided dashboards

### 8.2 Future Enhancement Candidates

These features may be considered for future phases:
- Machine learning-based complaint categorization
- Automated root cause analysis
- Benchmark comparison with industry standards
- Complaint resolution workflow tracking
- Customer satisfaction scoring integration
- Advanced drill-through capabilities
- Scheduled report distribution
- Data quality monitoring dashboard

---

## 9. Assumptions and Dependencies

### 9.1 Assumptions

| ID | Assumption | Impact if Invalid |
|----|------------|-------------------|
| A-001 | CSV file structure remains consistent with 14 defined columns | Requires data pipeline redesign |
| A-002 | Dataset contains fictional data only (no real customer PII) | Privacy/compliance implications |
| A-003 | Users have Power BI Desktop installed (for Power BI deliverable) | Cannot open .pbix file |
| A-004 | Users have modern web browsers (for React dashboard) | Compatibility issues |
| A-005 | Data volume remains under 10,000 records | Performance degradation |
| A-006 | Complaint IDs are intended to be unique (duplicates are errors) | Changes duplicate handling logic |
| A-007 | All 8 companies operate in same business context (fair comparison) | Misleading benchmarking |
| A-008 | Timely response targets are 90% or higher | Changes performance thresholds |

### 9.2 Dependencies

| ID | Dependency | Type | Mitigation |
|----|------------|------|------------|
| D-001 | Power BI Desktop software | External | Provide installation instructions |
| D-002 | CSV data file availability | Internal | Document data location |
| D-003 | Vercel hosting service | External | Document deployment process |
| D-004 | GitHub for version control | External | Create repository in advance |
| D-005 | Node.js and npm (for React development) | External | Document required versions |
| D-006 | Data cleaning script execution | Internal | Automate or document manual steps |
| D-007 | Business rule definitions (KPI calculations) | Internal | Document in TRD |

---

## 10. Risks and Limitations

### 10.1 Project Risks

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|-----------|--------|---------------------|
| **Data quality issues more severe than identified** | Medium | High | Implement robust validation and error handling |
| **Power BI performance with larger datasets** | Low | Medium | Test with 10K records; implement data model optimization |
| **React dashboard browser compatibility issues** | Low | Low | Test on all major browsers; polyfills as needed |
| **Unclear business requirements for KPI calculations** | Low | High | Validate definitions with stakeholders early |
| **Vercel deployment configuration challenges** | Low | Low | Follow Vercel documentation; test deployment early |
| **User adoption resistance** | Medium | High | Provide training, documentation, and champion users |
| **Scope creep with additional visualization requests** | High | Medium | Strict change control process; prioritize must-haves |

### 10.2 Technical Limitations

| Limitation | Impact | Workaround |
|------------|--------|------------|
| **Static data (no live updates)** | Dashboard shows point-in-time data | Document data refresh process |
| **Client-side data processing (React)** | Performance limits with large datasets | Implement pagination or server-side processing in future |
| **Power BI Desktop (not Power BI Service)** | No automatic refresh, limited sharing | Consider Power BI Service in future phase |
| **No authentication** | Anyone with URL can access React dashboard | Implement auth in future or use Vercel password protection |
| **Fictional data only** | Cannot validate with real-world scenarios | Ensure data represents realistic distributions |
| **Single data source (CSV)** | No integration with operational systems | Plan for future ETL pipeline |

### 10.3 Business Limitations

| Limitation | Impact | Consideration |
|------------|--------|---------------|
| **Company size not considered** | Higher complaint volumes may not indicate worse performance | Add disclaimer; consider per-capita metrics in future |
| **Timely response ≠ customer satisfaction** | Meeting SLA doesn't guarantee happy customers | Add satisfaction metrics in future phase |
| **No root cause attribution** | Can identify issues but not underlying causes | Requires manual investigation |
| **Historical data limited to 13 months** | Cannot identify long-term trends | Expand dataset in future |
| **No complaint severity weighting** | All complaints treated equally | Consider severity scoring in future |

---

## 11. Success Metrics and KPIs

### 11.1 Adoption Metrics

| Metric | Baseline | Target (30 days post-launch) |
|--------|----------|------------------------------|
| **Active Users** | 0 | 100% of target user group (15-20 users) |
| **Dashboard Opens per Week** | 0 | 50+ (Power BI + React combined) |
| **Average Session Duration** | N/A | 5-10 minutes |

### 11.2 Efficiency Metrics

| Metric | Baseline (Manual Process) | Target (With Dashboard) |
|--------|---------------------------|------------------------|
| **Time to Generate Weekly Report** | 2-3 hours | 5 minutes |
| **Time to Identify Complaint Spike** | 1-7 days | < 1 day |
| **Number of Ad-hoc Data Requests** | 10+ per week | < 3 per week |

### 11.3 Business Impact Metrics

| Metric | Baseline | Target (90 days post-launch) |
|--------|----------|------------------------------|
| **Timely Response Rate** | 90.08% | ≥ 92% |
| **Average Response Time** | 8.76 days | < 8 days |
| **Complaint Trend Identification Speed** | Reactive (after issues) | Proactive (early detection) |

### 11.4 Product Quality Metrics

| Metric | Target |
|--------|--------|
| **Dashboard Load Time** | < 3 seconds |
| **Data Accuracy** | 100% (validated against source CSV) |
| **User Satisfaction Score** | ≥ 4.0 / 5.0 |
| **Critical Bugs (post-launch)** | 0 |
| **Data Quality Pass Rate** | 100% (all validation rules passed) |

---

## 12. Compliance and Regulatory Considerations

### 12.1 Data Privacy

- **Status:** All data is fictional and for training purposes only
- **Requirement:** No real customer PII present in dataset
- **Validation:** Confirm with data provider that dataset is synthetic

### 12.2 Accessibility (React Dashboard)

- **Standard:** WCAG 2.1 Level AA compliance (goal)
- **Requirements:**
  - Keyboard navigation support
  - Screen reader compatibility
  - Sufficient color contrast
  - ARIA labels on interactive elements
- **Validation:** Accessibility audit using automated tools (Lighthouse, axe)

### 12.3 Data Retention

- **Original Data:** Preserve indefinitely in `data/original/`
- **Processed Data:** Maintain cleaning logs for audit purposes
- **Dashboard Files:** Version control with Git

---

## 13. Final Acceptance Criteria

The Financial Customer Complaint Analytics Platform will be considered **complete and accepted** when:

### 13.1 Power BI Deliverables

- [ ] **Deliverable:** Financial_Complaint_Analytics.pbix file
- [ ] **Location:** `powerbi/` directory
- [ ] **Content:**
  - 5 KPI cards (Total, Open, Closed, Timely Response Rate, Avg Response Time)
  - 4 visualizations (Monthly Trend, Product, Issue, Company Performance)
  - 3 interactive filters (Date, Company, Product)
  - Proper data model with relationships
  - All DAX measures implemented and tested
- [ ] **Quality:**
  - Professional formatting and layout
  - All visualizations respond correctly to filters
  - Data accuracy validated against source CSV
  - File opens without errors in Power BI Desktop

### 13.2 React Dashboard Deliverables

- [ ] **Deliverable:** React web application deployed to Vercel
- [ ] **GitHub Repository:** Code committed with proper structure
- [ ] **Production URL:** Accessible and functional
- [ ] **Content:**
  - 5 KPI cards matching Power BI
  - 4 charts matching Power BI visualizations
  - 3 filters with synchronization
  - Loading, empty, and error states
- [ ] **Quality:**
  - TypeScript strict mode with no errors
  - Responsive design (mobile, tablet, desktop)
  - Professional UI matching financial industry standards
  - Build succeeds without warnings

### 13.3 Data Processing Deliverables

- [ ] **Original Dataset:** Preserved in `data/original/lecture-file.csv`
- [ ] **Cleaned Dataset:** Stored in `data/processed/`
- [ ] **Data Cleaning Script:** Python or equivalent with documentation
- [ ] **Cleaning Log:** Detailed audit trail of all transformations
- [ ] **Quality:**
  - 25 duplicates identified and handled
  - Financial product names standardized (26 records cleaned)
  - 49 missing states preserved as NULL
  - 310 open complaints correctly flagged (after duplicate removal)
  - Date validations passed

### 13.4 Documentation Deliverables

- [ ] **PRD:** This document (PRD_Financial_Complaint_Analytics.md)
- [ ] **TRD:** Technical Requirements Document (TRD_Financial_Complaint_Analytics.md)
- [ ] **README:** Project overview with setup instructions
- [ ] **AI_USAGE.md:** Documentation of AI assistance (if applicable)
- [ ] **Data Dictionary:** Complete column definitions in TRD
- [ ] **User Guide:** Instructions for using dashboards (optional but recommended)

### 13.5 Testing and Validation

- [ ] **KPI Validation:** All 5 KPIs match expected calculations
  - Total Complaints: 4,975 (unique)
  - Open Complaints: 310 (6.23%)
  - Closed Complaints: 4,665 (93.77%)
  - Timely Response Rate: 90.08%
  - Average Response Time: 8.76 days
- [ ] **Filter Testing:** All filter combinations work correctly
- [ ] **Browser Testing:** React dashboard tested on Chrome, Firefox, Safari, Edge
- [ ] **Responsive Testing:** Mobile (375px), Tablet (768px), Desktop (1920px)
- [ ] **Data Accuracy:** Spot-check 20 random records between source and dashboard
- [ ] **Performance Testing:** Load time < 3 seconds, filter response < 1 second

### 13.6 Deployment Validation

- [ ] **Power BI:** File can be opened and used by stakeholders
- [ ] **React/Vercel:** Production URL accessible without errors
- [ ] **GitHub:** Repository properly structured and documented
- [ ] **Vercel Deployment:** Automatic deployment configured

---

## 14. Appendix

### 14.1 Glossary

| Term | Definition |
|------|------------|
| **Complaint** | A customer-reported issue with a financial product or service |
| **Open Complaint** | A complaint awaiting company response (response_status = "Open") |
| **Closed Complaint** | A complaint that has received a company response (response_status = "Closed") |
| **Timely Response** | A response provided within the required timeframe per regulatory requirements |
| **Response Time** | Number of days between complaint receipt and company response |
| **Financial Product** | Category of financial service (Credit card, Mortgage, etc.) |
| **Issue Category** | Type of problem reported (Unexpected fees, Fraudulent charges, etc.) |
| **Submission Channel** | Method customer used to submit complaint (Web, Phone, Mail, Referral) |

### 14.2 Acronyms

| Acronym | Definition |
|---------|------------|
| **KPI** | Key Performance Indicator |
| **PRD** | Product Requirements Document |
| **TRD** | Technical Requirements Document |
| **SLA** | Service Level Agreement |
| **BI** | Business Intelligence |
| **CSV** | Comma-Separated Values |
| **DAX** | Data Analysis Expressions (Power BI formula language) |
| **PII** | Personally Identifiable Information |
| **WCAG** | Web Content Accessibility Guidelines |
| **UI/UX** | User Interface / User Experience |

### 14.3 References

- **Dataset:** `lecture-file.csv` (5,000 records, 14 columns)
- **Data Analysis Script:** `analyze_data.py` (comprehensive dataset inspection)
- **Time Period:** October 2025 - October 2026 (13 months)
- **Companies:** 8 fictional financial service companies
- **Products:** 6 standardized financial product categories

### 14.4 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Product Manager** | ___________ | ___________ | ___________ |
| **Business Analyst Lead** | ___________ | ___________ | ___________ |
| **Technical Lead** | ___________ | ___________ | ___________ |
| **Operations Manager (Stakeholder)** | ___________ | ___________ | ___________ |

---

**End of Product Requirements Document**

---

**Document Classification:** Internal Use Only  
**Prepared By:** Product Management Team  
**Date:** November 22, 2026  
**Version:** 1.0
