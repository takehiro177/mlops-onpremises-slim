# /!\ WARNING: RESET EVERYTHING! 
# Remove all containers/networks/volumes/images and data in db
docker-compose down
docker system prune -f
docker volume prune -f
docker network prune -f

# rm -rf ./mnt/postgres/*  #  Linux ONLY
Remove-Item -Path ./mnt/postgres/* -Recurse  #  Windows PowerShell ONLY

# rm -rf ./mnt/airflow/logs/*  #  linux ONLY
Remove-Item -Path ./mnt/airflow/logs/* -Recurse  #  Windows PowerShell ONLY

# rm -rf ./mnt/mlflow/*  #  linux ONLY
Remove-Item -Path ./mnt/mlflow/* -Recurse  #  Windows PowerShell ONLY

docker rmi -f $(docker images -a -q)