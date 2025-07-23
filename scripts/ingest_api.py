def main():
    import pandas as pd
    import os
    from datetime import datetime
    import requests

    os.makedirs("data", exist_ok=True)

    def find_latest_available_month():
        current = datetime.today().replace(day=1)
        for _ in range(12):  # Try up to 12 months back
            month_str = current.strftime("%Y-%m")
            url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month_str}.parquet"
            response = requests.head(url)
            if response.status_code == 200:
                return month_str, url
            current = current.replace(day=1)
            current = current.replace(month=current.month - 1 if current.month > 1 else 12,
                                      year=current.year if current.month > 1 else current.year - 1)
        raise Exception("No available data found in the past 12 months.")

    month_str, url = find_latest_available_month()
    print(f"Found latest available month: {month_str}")
    print(f"Downloading from: {url}")

    df = pd.read_parquet(url, engine="pyarrow")
    output_path = f"data/yellow_tripdata_{month_str}.csv"
    df.to_csv(output_path, index=False)

    print(f"Downloaded {len(df):,} records and saved to {output_path}")

if __name__ == "__main__":
    main()

