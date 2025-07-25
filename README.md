# NYC Taxi ETL Pipeline

This project demonstrates an automated, production-grade Extract, Transform, and Load (ETL) pipeline developed to process and analyze New York City Yellow Taxi trip data. It emphasizes real-world data engineering and analytics practices suitable for FinOps, data engineering, and cloud analytics roles.

**Technology Stack:** Python, SQL, dbt, DuckDB, Prefect, Power BI

---

## Project Overview

The NYC Taxi ETL Pipeline automates data processing from extraction through to visualization-ready insights:

### Extraction

* Automatically fetches the latest monthly NYC Yellow Taxi data from a public cloud-hosted parquet file.

### Transformation

* Conducts comprehensive data cleaning (handling null values, type validations, duplicate removal) with Python's Pandas library.
* Implements business-logic-driven transformations and aggregations using modular SQL models built in dbt, generating summaries such as fare ranges, hourly trends, and daily statistics.

### Load and Export

* Loads the cleaned and transformed data into DuckDB, a high-performance analytical database.
* Exports curated analytics-ready datasets as CSV files:

  * `trip_summary.csv` (Daily summaries)
  * `hourly_summary.csv` (Hourly trends)
  * `fare_buckets.csv` (Fare distribution analysis)

### Orchestration

* Utilizes Prefect Cloud-managed infrastructure for workflow orchestration, ensuring automation, scheduling, monitoring, and task management.

---

## Repository Structure

```
nyc-taxi-etl/
├── etl_flow.py                   # Main orchestrator script (Prefect flow)
├── scripts/
│   ├── ingest_api.py             # Data ingestion from public API
│   ├── clean_data.py             # Data cleaning and validation
│   └── export_models.py          # Exporting models and datasets
├── taxi_dbt/
│   ├── models/                   # dbt SQL transformation models
│   └── schema.yml                # Documentation and schema definitions for dbt
├── requirements.txt              # Python dependencies
├── prefect.yaml                  # Deployment configurations for Prefect
└── README.md                     # Project documentation
```

---

## Analytical Insights

Visualizations and insights generated from the processed datasets include:

* **Daily Trip Volume and Revenue Trends**
* **Hourly Demand Patterns**
* **Fare Range Distribution Analysis**

*(Power BI dashboard screenshots or file link can be included here.)*

---

## Technical Specifications

| Layer           | Technology/Tools        |
| --------------- | ----------------------- |
| Language        | Python 3.12             |
| Data Ingestion  | Requests, PyArrow       |
| Data Cleaning   | Pandas                  |
| Data Modeling   | dbt, SQL                |
| Data Storage    | DuckDB                  |
| Orchestration   | Prefect (Cloud-managed) |
| Visualization   | Power BI                |
| Version Control | Git, GitHub             |

---

## Local Execution

To execute the pipeline locally, perform the following steps:

1. **Clone the repository:**

```bash
git clone https://github.com/Taaha-Yasrub/nyc-taxi-etl.git
cd nyc-taxi-etl
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the ETL pipeline:**

```bash
python etl_flow.py
```

*(Note: Ensure dbt and DuckDB are properly configured on your system.)*

---

## Project Relevance

This pipeline illustrates critical professional skills and processes:

* End-to-end data engineering pipeline design and automation
* Application of data quality checks and business logic transformations
* Implementation of modular SQL-based data modeling (dbt)
* Real-world workflow orchestration using cloud-native tools (Prefect)
* Integration with analytical dashboards (Power BI) to facilitate decision-making

---

## Contact

**Taaha Yasrub**

* [LinkedIn](https://www.linkedin.com/in/taaha-yasrub-ba9b04241/)
* [GitHub](https://github.com/Taaha-Yasrub)
