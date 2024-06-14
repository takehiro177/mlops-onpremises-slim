# mlops-onpremise-slim
> template for lightweight data pipeline and MLOps production environment

This template for data pipeline and MLOps is intended for lightweight batch process and limited amount of AI/ML models deployment.

The environment contains Airflow and MLflow with PostgreSQL backend, where each has its own backend db.

For full data pipeline and MLOps environment, extending the template by integrating Kubeflow, Hadoop, Hive, Apache Spark, and Feast are considered.

## Directory Tree
'''bash
├───docker
│   ├───airflow
│   ├───mlflow
│   └───postgres
│       └───entrypoint_initdb
└───mnt
    ├───airflow
    │   ├───dags
    │   │   ├───files
    │   │   ├───scripts
    │   │   │   
    │   │   └───sql
    │   │   
    │   ├───logs
    │   └───plugins
    ├───mlflow
    └───postgres
'''