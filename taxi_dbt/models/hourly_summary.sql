-- models/hourly_summary.sql

SELECT
  EXTRACT(HOUR FROM tpep_pickup_datetime) AS pickup_hour,
  COUNT(*) AS trip_count,
  ROUND(AVG(total_amount), 2) AS avg_fare
FROM yellow_tripdata_cleaned
GROUP BY pickup_hour
ORDER BY pickup_hour
