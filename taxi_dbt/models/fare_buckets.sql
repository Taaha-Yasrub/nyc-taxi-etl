-- models/fare_buckets.sql

SELECT
  CASE
    WHEN total_amount < 10 THEN 'Under $10'
    WHEN total_amount BETWEEN 10 AND 20 THEN '$10–$20'
    WHEN total_amount BETWEEN 20 AND 40 THEN '$20–$40'
    WHEN total_amount BETWEEN 40 AND 100 THEN '$40–$100'
    ELSE 'Over $100'
  END AS fare_range,
  COUNT(*) AS trip_count,
  ROUND(AVG(trip_distance), 2) AS avg_distance
FROM yellow_tripdata_cleaned
GROUP BY fare_range
ORDER BY trip_count DESC
