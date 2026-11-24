-- ============================================================================
-- SQL Query 4: Submission Channel Effectiveness Analysis
-- ============================================================================
-- Purpose: Compare complaint volumes and response quality across channels
-- Channels: Web, Phone, Postal mail, Referral, Fax, Email
-- ============================================================================

SELECT 
    submission_channel,
    COUNT(*) AS total_complaints,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) AS pct_of_total,
    
    -- Response status breakdown
    SUM(CASE WHEN response_status = 'Open' THEN 1 ELSE 0 END) AS open_count,
    SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) AS closed_count,
    ROUND(100.0 * SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS closure_rate,
    
    -- Timely response metrics
    SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) AS timely_yes,
    SUM(CASE WHEN timely_response = 'No' THEN 1 ELSE 0 END) AS timely_no,
    ROUND(100.0 * SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) / 
          NULLIF(SUM(CASE WHEN timely_response IN ('Yes', 'No') THEN 1 ELSE 0 END), 0), 2) AS timely_rate,
    
    -- Response time statistics
    ROUND(AVG(CASE WHEN response_status = 'Closed' THEN response_time_days END), 2) AS avg_response_days,
    ROUND(MIN(CASE WHEN response_status = 'Closed' THEN response_time_days END), 2) AS min_response_days,
    ROUND(MAX(CASE WHEN response_status = 'Closed' THEN response_time_days END), 2) AS max_response_days
FROM complaints_cleaned
GROUP BY submission_channel
ORDER BY total_complaints DESC;
