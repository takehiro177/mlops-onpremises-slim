# mlops-onpremises-slim

> A template for a lightweight data pipeline and MLOps production environment in a on-premises server.

This template is designed for organizations that require a streamlined and efficient approach to data pipeline and deploying AI/ML models on-premises environment. It is ideal for scenarios involving lightweight batch processing and deploying a limited number of models.

The environment includes Airflow and MLflow with a PostgreSQL backend, each with its own dedicated database. This ensures data integrity and provides a robust foundation for managing workflows and model tracking.

For organizations seeking a comprehensive data pipeline and MLOps environment, this template can be extended by integrating Kubeflow, Hadoop, Hive, Apache Spark, Apache Kafka, and Feast. These additional components enable advanced data processing, distributed computing, and feature engineering capabilities.

## System Diagram

<div style="width: 20%; height: 20%">
  
  ![system_diagram](images/mlops-onpremises-slim.png)
  
</div>


## Directory Structure

The project directory structure is as follows:

<pre>
.
│
├───docker
│   ├───airflow
│   │       Dockerfile
│   │       start-airflow.sh
│   │
│   ├───feast
│   │   │   data_sources.py
│   │   │   Dockerfile
│   │   │   entities.py
│   │   │   features.py
│   │   │   feature_services.py
│   │   │   feature_store.yaml
│   │   │   spark_push.ipynb
│   │   │
│   │   └───data
│   │           driver_stats.parquet
│   │           local_registry.db
│   │
│   ├───kafka
│   │       Dockerfile
│   │       driver_stats.parquet
│   │       kafka_sample.py
│   │
│   ├───mlflow
│   │       Dockerfile
│   │
│   └───postgres
│       │   Dockerfile
│       │
│       └───entrypoint_initdb
│               create-multiple-postgresql-databases.sh
│
├───images
│       mlops-onpremises-slim.png
│
└───mnt
    ├───airflow
    │   │   airflow.cfg
    │   │
    │   ├───dags
    │   │   │   README.md
    │   │   │   sample_feast_dag.py
    │   │   │   sample_mlflow_dag.py
    │   │   │   sample_postgres_dag.py
    │   │   │
    │   │   ├───files
    │   │   │       README.md
    │   │   │
    │   │   ├───nannyml
    │   │   │       README.md
    │   │   │
    │   │   ├───scripts
    │   │   │   │   sample_dag
    │   │   │   │
    │   │   │   └───__pycache__
    │   │   │           sample_postgres_dag.cpython-38.pyc
    │   │   │
    │   │   ├───sql
    │   │   │       birth_date.sql
    │   │   │       pet_schema.sql
    │   │   │       populate_pet_table.sql
    │   │   │
    │   │   └───__pycache__
    │   │           sample_feast_dag.cpython-38.pyc
    │   │           sample_mlflow_dag.cpython-38.pyc
    │   │           sample_postgres_dag.cpython-38.pyc
    │   │
    │   ├───feast
    │   ├───logs
    │   └───plugins
    │           README.md
    │
    ├───mlflow
    │       README.md
    │
    ├───postgres
    │   │   README.md
    │   │
    │   └───pgdata
    └───redis

</pre>

Thank you for reading my work!