-- ============================================================================
-- SQL Query 5: Temporal Trends Analysis (Monthly)
-- ============================================================================
-- Purpose: Track complaint volume and response quality over time
-- Date Range: October 2025 - October 2026 (13 months)
-- ============================================================================

SELECT 
    strftime('%Y-%m', date_received) AS month,
    COUNT(*) AS total_complaints,
    
    -- Response status
    SUM(CASE WHEN response_status = 'Open' THEN 1 ELSE 0 END) AS open_count,
    SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) AS closed_count,
    
    -- Timely response rate
    ROUND(100.0 * SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) / 
          NULLIF(SUM(CASE WHEN timely_response IN ('Yes', 'No') THEN 1 ELSE 0 END), 0), 2) AS timely_rate,
    
    -- Average response time
    ROUND(AVG(CASE WHEN response_status = 'Closed' THEN response_time_days END), 2) AS avg_response_days
FROM complaints_cleaned
GROUP BY strftime('%Y-%m', date_received)
ORDER BY month;
