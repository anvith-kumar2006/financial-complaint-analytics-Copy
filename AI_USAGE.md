# Data Analytics Project Documentation
## Financial Customer Complaint Analytics Platform

**Project Domain:** Financial Services Analytics  
**Role Demonstrated:** Data Analyst  
**Project Period:** November 2026  
**Primary Tools:** Python, SQL, Microsoft Power BI, React, TypeScript  
**Development Approach:** Independent analytical decisions with AI-assisted technical guidance

---

# 1. Project Overview

The Financial Customer Complaint Analytics Platform is an end-to-end data analytics project designed to transform raw financial customer complaint records into meaningful business insights.

The project focuses on analysing customer complaints, identifying recurring issues, evaluating company performance, monitoring response times and measuring the effectiveness of complaint resolution.

The objective is to demonstrate how data analytics can support business decision-making in the financial services sector.

The project follows an analytical workflow:

**Raw Data → Data Cleaning → Data Validation → SQL Analysis → KPI Development → Dashboarding → Business Insights**

The solution combines Python-based data processing, SQL-based analytical queries, an interactive React dashboard and a Microsoft Power BI report.

# 2. Business Problem

Financial institutions receive customer complaints across different products, companies, channels and geographical locations.

Without structured analysis, it can be difficult to identify:

- Which financial products generate the most complaints.
- Which complaint categories occur most frequently.
- How effectively companies resolve customer complaints.
- Whether companies respond within the required timeframe.
- How complaint volumes change over time.
- Which areas require operational improvement.

This project addresses these questions by developing a structured analytical solution that converts complaint records into measurable performance indicators.

# 3. Dataset and Data Understanding

The project began with a dataset containing 5,000 complaint records.

Initial data inspection identified 25 duplicate records. After removing duplicates, the final analytical dataset contained 4,975 unique complaint records.

### Data preparation summary

| Data quality activity | Result |
|---|---|
| Original records | 5,000 |
| Duplicate records identified | 25 |
| Records removed | 25 |
| Final cleaned records | 4,975 |
| Final unique records | 4,975 |

### Analytical dimensions

The dataset was used to analyse complaint information across dimensions such as:

- Financial products.
- Complaint issue categories.
- Financial companies.
- Geographic locations.
- Submission channels.
- Complaint submission dates.
- Response status.
- Timely response indicators.
- Response time in days.

The objective of data understanding was to identify the available analytical dimensions, assess data quality and establish a reliable foundation for further analysis.

# 4. Data Cleaning and Preparation

**Primary tools:** Python, Pandas

Data cleaning was an important part of the analytical workflow because inaccurate or duplicated records could affect the reliability of business KPIs.

### Data preparation activities

1. Inspected the original dataset structure.
2. Identified duplicate complaint IDs.
3. Removed duplicate records.
4. Standardised text fields and categories.
5. Validated and converted date fields.
6. Checked response-status consistency.
7. Calculated response time.
8. Generated cleaned analytical data.
9. Validated the final record count and KPI values.

### Key deliverables

- `clean_data.py`
- `data/processed/complaints_cleaned.csv`
- `data/processed/cleaning_log.json`
- `data/processed/validation_report.json`

The final processed dataset contains 4,975 unique complaint records.

**Analytical responsibility:** Data quality and consistency were treated as prerequisites for KPI calculation and reporting.

# 5. SQL-Based Data Analysis

**Primary tool:** SQL  
**Execution environment:** SQLite with Python

SQL was used to perform structured analytical queries on the cleaned complaint dataset.

Nine analytical query areas were developed.

| No. | Analysis | Business purpose |
|---:|---|---|
| 1 | KPI Summary | Understand overall complaint performance |
| 2 | Product Analysis | Identify products generating complaints |
| 3 | Geographic Analysis | Examine complaint distribution by location |
| 4 | Channel Effectiveness | Analyse complaint submission channels |
| 5 | Temporal Trends | Understand changes in complaint volumes |
| 6 | Issue Categories | Identify recurring customer problems |
| 7 | Company Performance | Compare complaint resolution performance |
| 8 | Response-Time Distribution | Examine response-time patterns |
| 9 | Product-Issue Matrix | Identify relationships between products and issues |

### SQL analytical techniques

The project used SQL operations and analytical logic involving:

- `SELECT`
- `WHERE`
- `GROUP BY`
- `ORDER BY`
- Aggregate functions.
- Conditional aggregation.
- Date-based grouping.
- Distinct record counting.
- Performance comparisons.

A Python execution script was used to load the cleaned dataset into an in-memory SQLite database and export analytical query results.

### Validation

The recorded SQL execution report shows that all nine queries completed successfully in that execution.

Selected SQL results were compared with Python calculations to check consistency.

**Deliverables:**

- Nine analytical SQL query files.
- SQL execution script.
- CSV and JSON result files.
- KPI validation outputs.

# 6. KPI Development and Business Metrics

A major part of the project involved defining measurable indicators to evaluate complaint performance.

The following KPI values were validated against the cleaned dataset.

### Overall performance indicators

| KPI | Value |
|---|---:|
| Total Complaints | 4,975 |
| Open Complaints | 310 |
| Closed Complaints | 4,665 |
| Timely Responses | 4,202 |
| Untimely Responses | 463 |
| Timely Response Rate | 90.08% |
| Average Response Time | 8.76 days |

### KPI interpretation

**Total Complaints**

Measures the total number of unique customer complaint records.

**Open Complaints**

Measures complaints that have not reached a closed response status.

**Closed Complaints**

Measures complaints recorded as closed.

**Timely Response Rate**

Measures the percentage of responses recorded as timely among records with a Yes or No timely-response indicator.

\[
\text{Timely Response Rate} =
\frac{\text{Timely Responses}}
{\text{Timely Responses}+\text{Untimely Responses}}
\times 100
\]

\[
= \frac{4202}{4202+463}\times100
=90.08\%
\]

**Average Response Time**

Measures the average number of days taken to respond to complaints, based on the available response-time data.

\[
\text{Average Response Time} = 8.76 \text{ days}
\]

These KPIs provide a quantitative foundation for evaluating complaint volumes, operational status and response performance.

# 7. Microsoft Power BI Dashboard

**Tool:** Microsoft Power BI Desktop

The Power BI dashboard was personally developed by me using Microsoft Power BI Desktop.

This was a hands-on business intelligence implementation, not an autonomously generated dashboard.

### My implementation responsibilities

- Imported the cleaned CSV dataset into Power BI.
- Checked the imported columns and data types.
- Configured the data model.
- Created DAX measures for the required KPIs.
- Personally implemented the Total Complaints measure.
- Personally implemented Open Complaints and Closed Complaints measures.
- Created the Timely Response Rate measure.
- Created the Average Response Time measure.
- Designed and formatted KPI cards.
- Created monthly complaint trend visualisations.
- Built financial product distribution charts.
- Developed Top 10 issue-category analysis.
- Created company performance visualisations.
- Configured Date, Company and Financial Product slicers.
- Tested interactive filtering and KPI changes.
- Saved the completed report as `Financial_Complaint_Analytics.pbix`.
- Published the report to Power BI Service.

### Dashboard capabilities

| Visualisation | Analytical purpose |
|---|---|
| KPI Cards | Display overall performance |
| Monthly Trend | Track complaint volume over time |
| Product Distribution | Compare complaint volumes by product |
| Top Issue Categories | Identify frequent complaint issues |
| Company Performance | Compare company-level indicators |
| Interactive Slicers | Filter data by date, company and product |

### DAX and KPI implementation

The dashboard uses DAX measures to calculate and display key performance indicators.

Example of the Total Complaints measure:

```dax
Total Complaints =
DISTINCTCOUNT('complaints_cleaned'[complaint_id])
```

Example of the Average Response Time measure:

```dax
Average Response Time =
AVERAGE('complaints_cleaned'[response_time_days])
```

The Power BI dashboard was manually configured and tested by me. AI assistance was limited to technical explanations, DAX guidance and troubleshooting during implementation.

# 8. React Analytics Dashboard

**Technology stack:**

- React
- TypeScript
- Vite
- Tailwind CSS
- Recharts
- Lucide React

The React dashboard provides an additional interface for exploring complaint analytics.

### Main analytical features

- KPI summary cards.
- Product-wise complaint analysis.
- Geographic complaint distribution.
- Submission-channel analysis.
- Monthly complaint trends.
- Response-time analysis.
- Issue-category table.
- Interactive data presentation.

The application uses the cleaned complaint data to display analytical summaries and visualisations.

The Power BI Dashboard tab provides a downloadable `.pbix` report for users who want to explore the report in Microsoft Power BI Desktop.

# 9. Data Validation and Testing

Data validation was performed to improve the reliability of the analytical results.

### Validation activities

1. Checked the cleaned dataset record count.
2. Verified duplicate removal.
3. Compared KPI calculations.
4. Checked selected SQL results against Python calculations.
5. Reviewed dashboard KPI values.
6. Tested interactive slicer behaviour.
7. Reviewed data compatibility with the React dashboard.

### Recorded test results

The project test report records the following results:

| Test category | Passed checks |
|---|---:|
| KPI Validation | 7/7 |
| SQL-Python Consistency | 5/5 |
| Data Quality | 5/5 |
| React Data Compatibility | 3/3 |
| **Total** | **20/20** |

These figures represent the checks recorded in the project test report, not a claim of complete test coverage.

# 10. Business Analysis and Insights

The analytical structure enables several important business questions to be investigated.

### Complaint volume analysis

Identify which financial products and issue categories contribute the highest complaint volumes.

### Company performance analysis

Compare complaint volumes, closure rates and timely response performance across financial companies.

### Operational efficiency

Use response-time metrics to understand how quickly complaints are being addressed.

### Temporal analysis

Examine complaint trends across months to identify changes in complaint activity.

### Product and issue relationship

Use the product-issue matrix to identify recurring problems associated with particular financial products.

The project establishes the analytical framework for these investigations. Specific business recommendations should be based on the corresponding filtered results and validated observations.

# 11. AI Tools and Human Contribution

AI tools were used as supporting resources during development. They did not replace the analytical decisions, manual dashboard development or validation performed by the project author.

### AI-assisted activities

| Area | AI contribution |
|---|---|
| Requirements | Documentation and planning assistance |
| Python | Code-generation and debugging assistance |
| SQL | Query-development assistance |
| React | Frontend implementation assistance |
| Power BI | DAX explanations and troubleshooting guidance |
| Documentation | Technical writing and project documentation |
| Deployment | GitHub and Vercel configuration guidance |

### My contributions

| Area | My contribution |
|---|---|
| Project definition | Defined the project objective and analytical scope |
| Data understanding | Reviewed the dataset and analytical requirements |
| Data preparation | Reviewed cleaning logic and validated processed outputs |
| SQL analytics | Reviewed query requirements and analytical results |
| KPI development | Defined and validated the required business metrics |
| Power BI | Personally created DAX measures, KPI cards, charts and slicers |
| Dashboard testing | Tested visualisations and interactive filters |
| Project management | Made implementation and deployment decisions |

**The Power BI KPI measures and dashboard were personally implemented by me.** AI assistance provided explanations and troubleshooting support, rather than independently creating the report.

# 12. Technical Skills Demonstrated

This project demonstrates practical application of the following data analytics skills.

| Skill area | Technologies / concepts |
|---|---|
| Data Cleaning | Python, Pandas |
| Data Quality | Duplicate detection, validation, consistency checks |
| Data Analysis | Exploratory analysis and KPI calculation |
| SQL | Aggregations, filtering, grouping and analytical queries |
| Business Intelligence | Microsoft Power BI |
| DAX | Measures and KPI calculations |
| Data Visualisation | Power BI, Recharts |
| Dashboard Development | Interactive filters, KPI cards and charts |
| Data Validation | Python-SQL result comparison |
| Documentation | Analytical and technical documentation |
| Deployment | GitHub and Vercel preparation |

# 13. Future Improvements

Potential enhancements include:

- More detailed company benchmarking.
- Advanced complaint trend analysis.
- Predictive analysis of complaint volumes.
- Natural Language Processing for complaint descriptions.
- Automated dataset refresh.
- More detailed executive reporting.
- Secure Power BI embedding within the React application.

These are proposed future improvements, not currently completed features.

# 14. Conclusion

The Financial Customer Complaint Analytics Platform demonstrates an end-to-end approach to financial complaint data analysis.

The project covers the major stages of an analytical workflow, from raw dataset inspection and cleaning to SQL querying, KPI development, interactive dashboard creation and result validation.

A key part of the implementation was the independent development of the Microsoft Power BI dashboard, including DAX measures, KPI cards, analytical visualisations and interactive slicers.

Through this project, I applied Python, SQL and Power BI to a practical financial-services dataset and developed an understanding of how structured data analysis can support business monitoring and decision-making.

---

**Document Version:** 3.0  
**Project:** Financial Customer Complaint Analytics Platform  
**Primary Analytical Tools:** Python, SQL and Microsoft Power BI  
**Frontend:** React and TypeScript  
**Development Approach:** Human-led analytical implementation with AI-assisted technical support