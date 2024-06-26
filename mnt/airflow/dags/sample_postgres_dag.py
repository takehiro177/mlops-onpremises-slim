from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

import datetime
import os
# [START postgres_sql_execute_query_operator_howto_guide]


# create_pet_table, populate_pet_table, and get_birth_date are examples of tasks created by
# instantiating the Postgres Operator

DAG_ID = "postgres_operator_dag"


with DAG(
    dag_id=DAG_ID,
    start_date=datetime.datetime(2024, 6, 10),
    schedule=None,
    catchup=False,
) as dag:
    create_pet_table = SQLExecuteQueryOperator(
    task_id="create_pet_table",
    conn_id="postgres_dwh",
    sql="sql/pet_schema.sql",
    )
    
    populate_pet_table = SQLExecuteQueryOperator(
    task_id="populate_pet_table",
    conn_id="postgres_dwh",
    sql="sql/populate_pet_table.sql",
    )

    get_birth_date = SQLExecuteQueryOperator(
        task_id="get_birth_date",
        conn_id="postgres_dwh",
        sql="sql/birth_date.sql",
        params={"begin_date": "2020-01-01", "end_date": "2020-12-31"},
        hook_params={"options": "-c statement_timeout=3000ms"},
    )

    create_pet_table >> populate_pet_table >> get_birth_date
    # [END postgres_sql_execute_query_operator_howto_guide]