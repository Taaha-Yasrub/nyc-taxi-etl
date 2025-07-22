-- models/trip_summary.sql

SELECT
  DATE(tpep_pickup_datetime) AS trip_date,
  COUNT(*) AS trip_count,
  ROUND(AVG(total_amount), 2) AS avg_fare,
  ROUND(AVG(trip_distance), 2) AS avg_distance
FROM yellow_tripdata_cleaned
GROUP BY trip_date
ORDER BY trip_date
