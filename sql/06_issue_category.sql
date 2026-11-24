-- ============================================================================
-- SQL Query 6: Issue Category Deep Dive
-- ============================================================================
-- Purpose: Analyze complaint distribution and resolution by issue type
-- Insights: Identify most problematic issue categories
-- ============================================================================

SELECT 
    issue_category,
    COUNT(*) AS total_complaints,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) AS pct_of_total,
    
    -- Response status
    SUM(CASE WHEN response_status = 'Open' THEN 1 ELSE 0 END) AS open_count,
    SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) AS closed_count,
    ROUND(100.0 * SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS closure_rate,
    
    -- Timely response
    ROUND(100.0 * SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) / 
          NULLIF(SUM(CASE WHEN timely_response IN ('Yes', 'No') THEN 1 ELSE 0 END), 0), 2) AS timely_rate,
    
    -- Response time
    ROUND(AVG(CASE WHEN response_status = 'Closed' THEN response_time_days END), 2) AS avg_response_days
FROM complaints_cleaned
GROUP BY issue_category
ORDER BY total_complaints DESC
LIMIT 20;
