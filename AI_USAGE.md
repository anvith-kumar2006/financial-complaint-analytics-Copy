# AI Usage Documentation

## Financial Customer Complaint Analytics Platform

## 1. Overview

This document describes how artificial intelligence (AI) tools supported the planning, development, implementation, testing, documentation, and deployment preparation of the **Financial Customer Complaint Analytics Platform**.

The project uses Python, SQL, React, TypeScript, and Microsoft Power BI. AI tools assisted with development; human decisions, review, validation, and the documented manual Power BI Desktop work remained part of the process.

### AI tools used

| Tool | Purpose |
|---|---|
| Kiro AI (Claude Sonnet 4.5) | Project planning, code-generation assistance, debugging, and documentation |
| ChatGPT | Technical guidance, implementation assistance, and Power BI troubleshooting |

**Project development period:** November 2026

**Development approach:** AI-assisted development with human supervision and validation.

## 2. Executive summary

AI tools assisted at multiple points in the project lifecycle, including requirements analysis, data processing, SQL analytics, React and TypeScript development, testing, documentation, and deployment preparation.

Human contributions included defining project requirements, providing the dataset, reviewing outputs, validating results, making development decisions, and manually creating the Power BI report in Power BI Desktop. The work followed an iterative human-AI collaboration process and was not fully autonomous.

## 3. Development phases

### Phase 0: Requirements analysis and planning

**AI contributions**

- Analyzed the original complaint dataset, which contained 5,000 records.
- Identified 25 duplicate records.
- Assisted with establishing the cleaned dataset baseline.
- Prepared the Product Requirements Document (PRD) and Technical Requirements Document (TRD).
- Assisted with defining the project architecture and implementation workflow.

**Deliverables**

- PRD v1.0
- TRD v1.0
- Initial data analysis script

**Human contributions**

- Defined the project objective.
- Provided the original dataset.
- Reviewed the requirements and architecture.

### Phase 0.5: Documentation audit and correction

Document validation identified inconsistencies between the PRD and TRD.

**AI contributions**

- Assisted with data reconciliation scripts and cross-checks of complaint counts and KPI calculations.
- Helped correct outdated baseline references and update the PRD and TRD to version 1.1.
- Prepared a final verification report.

**Validated baselines**

| Metric | Value |
|---|---:|
| Total complaints | 4,975 |
| Open complaints | 310 |
| Closed complaints | 4,665 |
| Timely responses | 4,202 |
| Untimely responses | 463 |
| Timely response rate | 90.08% |
| Average response time | 8.76 days |

These are the documented Python/SQL validation values in `data/processed/validation_report.json` and `test_results.json`.

**Human contributions**

- Identified inconsistencies in the initial documents and requested further validation.
- Reviewed the corrected documentation and approved proceeding to implementation.

### Phase 1: Data processing pipeline

**AI contributions**

AI assistance supported development of the Python data-cleaning pipeline, including:

- Duplicate complaint ID removal.
- Whitespace and category standardization.
- Date validation and conversion.
- Response-status consistency checks.
- Response-time calculation.
- KPI validation, cleaning logs, and validation reports.

**Key deliverables**

- `clean_data.py`
- `data/processed/complaints_cleaned.csv`
- `data/processed/cleaning_log.json`
- `data/processed/validation_report.json`

The cleaned dataset contains 4,975 unique complaint records. The pipeline reads `data/original/lecture-file.csv`; the raw source dataset is not included in the public Git repository.

**Human contributions**

- Reviewed the data-cleaning strategy and generated outputs.
- Confirmed the validated KPI baselines.

### Phase 2: SQL analytics

**AI contributions**

AI assistance supported development of nine analytical SQL queries:

| Query | Analysis |
|---|---|
| 01 | KPI summary |
| 02 | Product analysis |
| 03 | Geographic analysis |
| 04 | Channel effectiveness |
| 05 | Temporal trends |
| 06 | Issue categories |
| 07 | Company performance |
| 08 | Response-time distribution |
| 09 | Product-issue matrix |

A Python SQL execution script loads the cleaned CSV into an in-memory SQLite database and exports query results.

**Deliverables**

- Nine SQL query files.
- SQL execution script.
- CSV and JSON query results.
- KPI validation outputs.

**Recorded validation**

- `sql/results/execution_summary.json` records that all nine queries completed successfully in that run.
- Recorded SQL results were compared with Python calculations for selected KPIs.
- Query column-name mismatches identified during development were corrected.

These are results from the recorded run, not a guarantee that every future execution will succeed.

**Human contributions**

- Reviewed analytical requirements and query outputs.
- Approved using the generated results in dashboard development.

### Phase 3: React web dashboard

**AI contributions**

AI assistance supported implementation of the React analytics dashboard.

**Technology stack**

- React 18
- TypeScript
- Vite
- Tailwind CSS
- Recharts
- Lucide React

**Major components**

| Component | Functionality |
|---|---|
| KPI Cards | Complaint performance indicators |
| Product Chart | Product-wise complaint analysis |
| State Chart | Geographic complaint distribution |
| Channel Chart | Submission-channel analysis |
| Trends Chart | Monthly complaint trends |
| Response Time Chart | Response-time distribution |
| Issue Table | Issue-category analysis |

Other implementation work included CSV loading, client-side calculations, responsive layout, component organization, and loading/error handling.

**Human contributions**

- Reviewed and tested the interface.
- Identified visualization and presentation issues.
- Requested corrections and improvements.

### Phase 4: Power BI dashboard

The project documentation distinguishes the manually authored Power BI Desktop report from the React implementation. The report was created in Microsoft Power BI Desktop with AI guidance; it was not generated autonomously.

**AI contributions**

- Prepared Power BI setup instructions and DAX measure guidance.
- Guided data import and data-type validation.
- Assisted with KPI cards, trend and product visuals, issue analysis, and slicer configuration.
- Helped check KPI values and slicer interactions.

**Human contributions**

- Imported the cleaned CSV into Power BI Desktop.
- Configured the data model and measures.
- Created, arranged, and formatted report visuals.
- Tested interactive slicers.
- Saved the report as `Financial_Complaint_Analytics.pbix`.
- Project documentation records publishing the report to Power BI Service.

**Final KPI baselines**

- Total complaints: 4,975
- Open complaints: 310
- Closed complaints: 4,665
- Timely response rate: 90.08%
- Average response time: 8.76 days

The React application's Power BI Dashboard tab offers the `.pbix` file as a download. It does not embed or render the report. Opening the downloaded report requires Power BI Desktop; access to Power BI Service depends on the user's account and permissions.

### Phase 5: Testing and validation

**AI contributions**

AI assistance supported validation work in four areas:

1. KPI baseline validation.
2. SQL-Python consistency.
3. Data quality.
4. React data compatibility.

At the time of the recorded `test_results.json`, the report showed:

| Test category | Recorded checks passed |
|---|---:|
| KPI validation | 7/7 |
| SQL-Python consistency | 5/5 |
| Data quality | 5/5 |
| React data compatibility | 3/3 |
| Total | 20/20 |

These results describe the recorded checks only. They are not a claim of 100% test coverage or a guarantee of error-free operation in every environment.

**Human contributions**

- Reviewed test outputs and dashboard calculations.
- Tested interactive filters.
- Identified interface issues during implementation.

### Phase 6: Documentation and deployment preparation

**AI contributions**

- Assisted with the main README and project setup instructions.
- Documented analytical methods and integration details.
- Assisted with GitHub configuration and Vercel deployment preparation.

**Human contributions**

- Reviewed project documentation.
- Managed the documented Power BI publishing process.
- Made deployment decisions and reviewed the application experience.

The React dashboard is a static Vite application configured for Vercel. Deployment outcome depends on the hosting account and deployment configuration; no guarantee of production readiness is implied.

## 4. AI capabilities demonstrated

### 4.1 Data analysis and processing

AI assistance included dataset inspection, duplicate identification, data-cleaning logic, KPI calculations, and validation-script development.

### 4.2 Full-stack development

AI-assisted implementation covered Python data processing, SQL queries, React and TypeScript frontend components, and dashboard integration.

### 4.3 Debugging and problem solving

AI tools assisted with investigating SQL column-name mismatches, TypeScript errors, JSON serialization, visualization behavior, and dashboard integration issues.

### 4.4 Business intelligence

AI guidance supported DAX measures, KPI visualization, monthly trends, product and issue analysis, and interactive report filtering.

### 4.5 Documentation and deployment

AI assistance supported technical documentation, GitHub preparation, and Vercel configuration notes.

## 5. Human-AI collaboration

The project used AI as a development assistant with human review and direction.

**Human responsibilities**

1. Defining the project idea and objectives.
2. Selecting and providing the dataset.
3. Reviewing requirements.
4. Validating analytical results.
5. Making dashboard design decisions.
6. Manually implementing the Power BI report.
7. Making testing and deployment decisions.

**AI-assisted responsibilities**

1. Requirements documentation.
2. Code-generation assistance.
3. Data-processing and SQL implementation assistance.
4. React implementation assistance.
5. Debugging guidance.
6. DAX and Power BI guidance.
7. Documentation preparation.

## 6. Challenges and lessons learned

**Challenges**

- Identifying duplicate records and inconsistent KPI references.
- Keeping Python and SQL calculations consistent.
- Resolving TypeScript build issues.
- Handling date hierarchies and slicers in Power BI.
- Understanding the distinction between a Power BI Desktop report and a web-embedded report.
- Preparing a frontend-only Vercel deployment.

**Lessons learned**

1. Validate data before creating visualizations.
2. Maintain a single authoritative KPI baseline.
3. Use modular code for maintainability.
4. Verify generated code through execution.
5. Keep business logic consistent across analytical platforms.
6. Treat AI as an assistant and retain human oversight.

## 7. Future enhancement opportunities

Potential future work includes secure Power BI embedding, automated dataset refresh, complaint trend analysis, natural language processing, automated report generation, additional visualizations, and backend data integration. These are possibilities, not claims about current functionality.

## 8. Conclusion

The Financial Customer Complaint Analytics Platform combines Python data processing, SQL analytics, a React dashboard, and a manually authored Microsoft Power BI report. AI tools assisted with implementation and documentation, while human contributions included requirements, review and validation, project decisions, and hands-on Power BI Desktop work.

---

**Document version:** 2.0
**Last updated:** November 2026
**Primary AI development tool:** Kiro AI (Claude Sonnet 4.5)
**Additional AI assistance:** ChatGPT
**Project:** Financial Customer Complaint Analytics Platform
