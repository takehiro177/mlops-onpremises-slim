# /!\ WARNING: RESET EVERYTHING! 
# Remove all containers/networks/volumes/images and data in db
docker-compose down
docker system prune -f
docker volume prune -f
docker network prune -f

#rm -rf ./mnt/postgres/!(README.md)  #  linux ONLY
Remove-Item -Path ./mnt/postgres/pgdata/* -Exclude README.md -Recurse  #  Windows PowerShell ONLY

# rm -rf ./mnt/airflow/logs/!(README.md)  #  linux ONLY
Remove-Item -Path ./mnt/airflow/logs/* -Exclude README.md -Recurse  #  Windows PowerShell ONLY

# rm -rf ./mnt/airflow/dags/files/!(README.md)  #  linux ONLY
Remove-Item -Path ./mnt/airflow/dags/files/* -Exclude README.md -Recurse  #  Windows PowerShell ONLY

# rm -rf ./mnt/mlflow/!(README.md)  #  linux ONLY
Remove-Item -Path ./mnt/mlflow/* -Exclude README.md -Recurse  #  Windows PowerShell ONLY

# rm -rf ./mnt/redis/!(README.md)  #  linux ONLY
Remove-Item -Path ./mnt/redis/* -Exclude README.md -Recurse  #  Windows PowerShell ONLY

docker rmi -f $(docker images -a -q)