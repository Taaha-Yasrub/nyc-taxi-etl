def main():
    import pandas as pd
    import os
    from datetime import datetime

    files = sorted(os.listdir("data"), reverse=True)
    latest_file = next((f for f in files if f.endswith(".csv") and "-cleaned" not in f), None)

    if latest_file:
        input_path = os.path.join("data", latest_file)
        output_path = input_path.replace(".csv", "-cleaned.csv")
        print(f"Cleaning {input_path}...")

        df = pd.read_csv(input_path)
        df = df.dropna(subset=["tpep_pickup_datetime", "tpep_dropoff_datetime"])
        df = df.drop_duplicates()

        numeric_columns = ["passenger_count", "trip_distance", "fare_amount", "total_amount"]
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df = df.dropna(subset=numeric_columns)

        df.to_csv(output_path, index=False)
        print(f"Cleaned and saved to {output_path}")
    else:
        print("No latest raw CSV found to clean.")

if __name__ == "__main__":
    main()
