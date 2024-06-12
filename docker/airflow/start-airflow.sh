#!/usr/bin/env bash

# Move to the AIRFLOW HOME directory
cd $AIRFLOW_HOME

# Export environement variables
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# Initiliase the metadatabase
airflow db init

# Create User
airflow users create -e "mlops@mlops.com" -f "mlops" -l "mlops" -p "mlops" -r "Admin" -u "takehiro"

# Run the scheduler in background
airflow scheduler &> /dev/null &

# Run the scheduler in foreground (for docker logs)
#exec airflow scheduler

# Run the web sever in foreground (for docker logs)
exec airflow webserver