#!/usr/bin/env bash

# Move to the AIRFLOW HOME directory
cd $AIRFLOW_HOME

# initialize feast
#feast init my_project

# Export environement variables
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# Initiliase the metadatabase
airflow db migrate

# Create User
airflow users create -e "mlops@mlops.com" -f "mlops" -l "mlops" -p "mlops" -r "Admin" -u "takehiro"

# Run the scheduler in background
airflow scheduler &> /dev/null &

# Run the web sever in foreground (for docker logs)
exec airflow webserver

# add connection to postgres db
airflow connections add 'postgres_dwh' --conn-json '{"conn_type": "postgres", "login": "mlops", "password": "mlops", "host": "postgres", "port": 5432}'