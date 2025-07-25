from prefect import flow, task
from scripts import ingest_api, clean_data, export_models

@task
def ingest_data_task():
    ingest_api.main()

@task
def clean_data_task():
    clean_data.main()

@task
def run_dbt_models():
    import subprocess
    subprocess.run(["dbt", "run"], cwd="taxi_dbt", check=True)

@task
def export_results_task():
    export_models.main()

@flow(name="NYC Taxi Full ETL Pipeline")
def taxi_pipeline():
    print("Starting full pipeline...")
    ingest_data_task()
    clean_data_task()
    run_dbt_models()
    export_results_task()
    print("All steps completed!")

if __name__ == "__main__":
    taxi_pipeline()
