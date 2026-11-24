-- ============================================================================
-- SQL Query 1: KPI Summary Dashboard
-- ============================================================================
-- Purpose: Calculate all primary KPIs for executive dashboard
-- Expected Results:
--   Total: 4,975 | Open: 310 | Closed: 4,665
--   Timely Rate: 90.08% | Avg Response: 8.76 days
-- ============================================================================

SELECT 
    COUNT(*) AS total_complaints,
    SUM(CASE WHEN response_status = 'Open' THEN 1 ELSE 0 END) AS open_complaints,
    SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) AS closed_complaints,
    ROUND(100.0 * SUM(CASE WHEN response_status = 'Open' THEN 1 ELSE 0 END) / COUNT(*), 2) AS open_rate,
    ROUND(100.0 * SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS closed_rate,
    
    -- Timely response metrics (only for closed with timely_response flag)
    SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) AS timely_yes,
    SUM(CASE WHEN timely_response = 'No' THEN 1 ELSE 0 END) AS timely_no,
    ROUND(100.0 * SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) / 
          (SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) + 
           SUM(CASE WHEN timely_response = 'No' THEN 1 ELSE 0 END)), 2) AS timely_rate,
    
    -- Average response time (only for closed complaints)
    ROUND(AVG(CASE WHEN response_status = 'Closed' THEN response_time_days END), 2) AS avg_response_days,
    MIN(CASE WHEN response_status = 'Closed' THEN response_time_days END) AS min_response_days,
    MAX(CASE WHEN response_status = 'Closed' THEN response_time_days END) AS max_response_days
FROM complaints_cleaned;
