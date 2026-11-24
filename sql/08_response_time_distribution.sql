-- ============================================================================
-- SQL Query 8: Response Time Distribution Analysis
-- ============================================================================
-- Purpose: Analyze response time buckets for closed complaints
-- Insights: Understand response time patterns and SLA adherence
-- ============================================================================

SELECT 
    CASE 
        WHEN response_time_days <= 3 THEN '0-3 days'
        WHEN response_time_days <= 7 THEN '4-7 days'
        WHEN response_time_days <= 15 THEN '8-15 days'
        WHEN response_time_days <= 30 THEN '16-30 days'
        ELSE '30+ days'
    END AS response_time_bucket,
    COUNT(*) AS complaint_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) AS pct_of_closed,
    
    -- Timely response breakdown
    SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) AS timely_yes,
    SUM(CASE WHEN timely_response = 'No' THEN 1 ELSE 0 END) AS timely_no,
    ROUND(100.0 * SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) / 
          NULLIF(COUNT(*), 0), 2) AS timely_rate_in_bucket,
    
    -- Stats within bucket
    ROUND(AVG(response_time_days), 2) AS avg_days_in_bucket,
    MIN(response_time_days) AS min_days_in_bucket,
    MAX(response_time_days) AS max_days_in_bucket
FROM complaints_cleaned
WHERE response_status = 'Closed' AND response_time_days IS NOT NULL
GROUP BY response_time_bucket
ORDER BY 
    CASE response_time_bucket
        WHEN '0-3 days' THEN 1
        WHEN '4-7 days' THEN 2
        WHEN '8-15 days' THEN 3
        WHEN '16-30 days' THEN 4
        ELSE 5
    END;
