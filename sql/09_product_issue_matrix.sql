-- ============================================================================
-- SQL Query 9: Product-Issue Matrix Analysis
-- ============================================================================
-- Purpose: Cross-tabulation of products vs issues to identify problem areas
-- Insights: Which products have which types of issues most frequently
-- ============================================================================

SELECT 
    financial_product,
    issue_category,
    COUNT(*) AS complaint_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(PARTITION BY financial_product), 2) AS pct_of_product,
    
    -- Response metrics
    ROUND(100.0 * SUM(CASE WHEN response_status = 'Closed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS closure_rate,
    ROUND(100.0 * SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) / 
          NULLIF(SUM(CASE WHEN timely_response IN ('Yes', 'No') THEN 1 ELSE 0 END), 0), 2) AS timely_rate,
    ROUND(AVG(CASE WHEN response_status = 'Closed' THEN response_time_days END), 2) AS avg_response_days
FROM complaints_cleaned
GROUP BY financial_product, issue_category
HAVING COUNT(*) >= 5  -- Only combinations with 5+ complaints
ORDER BY financial_product, complaint_count DESC;
