# Base Image
FROM python:3.8-slim-buster

WORKDIR /mlflow

RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    pip install mlflow psycopg2

ENV BACKEND_URI postgresql+psycopg2://mlops:mlops@postgres:5432/mlops_db

EXPOSE 5000

CMD mlflow ui --backend-store-uri $BACKEND_URI --host 0.0.0.0 --port 5000 --default-artifact-root file:mlruns-artifacts/
