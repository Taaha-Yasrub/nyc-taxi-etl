def main():
    import duckdb
    import os

    con = duckdb.connect("taxi_dbt/data/taxi.duckdb")

    expected_columns = [
        "VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count",
        "trip_distance", "RatecodeID", "store_and_fwd_flag", "PULocationID",
        "DOLocationID", "payment_type", "fare_amount", "extra", "mta_tax",
        "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount",
        "congestion_surcharge", "airport_fee"
    ]

    con.execute("DROP TABLE IF EXISTS yellow_tripdata_cleaned")

    data_dir = "data"
    for filename in os.listdir(data_dir):
        if filename.endswith("-cleaned.csv"):
            path = os.path.join(data_dir, filename)
            print(f"📥 Loading {filename} into DuckDB...")
            try:
                con.execute(f"""
                    CREATE OR REPLACE TABLE yellow_tripdata_cleaned AS
                    SELECT {', '.join(expected_columns)}
                    FROM read_csv_auto('{path}', HEADER=TRUE)
                """)
            except duckdb.CatalogException:
                con.execute(f"""
                    INSERT INTO yellow_tripdata_cleaned
                    SELECT {', '.join(expected_columns)}
                    FROM read_csv_auto('{path}', HEADER=TRUE)
                """)

    tables = ['trip_summary', 'hourly_summary', 'fare_buckets']
    for table in tables:
        output = f"{table}.csv"
        con.execute(f"""
            COPY (SELECT * FROM {table})
            TO '{output}'
            WITH (HEADER, DELIMITER ',')
        """)
        print(f"✅ Exported {table} to {output}")

if __name__ == "__main__":
    main()
