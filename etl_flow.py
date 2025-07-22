from prefect import flow, task
import subprocess

@task
def ingest_data():
    subprocess.run(["python", "scripts/ingest_api.py"], check=True)

@task
def clean_data():
    subprocess.run(["python", "scripts/clean_data.py"], check=True)

@task
def run_dbt_models():
    subprocess.run(["dbt", "run"], cwd="taxi_dbt", check=True)

@task
def export_results():
    subprocess.run(["python", "scripts/export_models.py"], check=True)

@flow(name="NYC Taxi Full ETL Pipeline")
def taxi_pipeline():
    print("Starting full pipeline...")
    ingest_data()
    clean_data()
    run_dbt_models()
    export_results()
    print("All steps completed!")

if __name__ == "__main__":
    taxi_pipeline()
