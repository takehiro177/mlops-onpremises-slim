# Base Image
FROM python:3.8-slim-buster

WORKDIR /mlflow

RUN pip install mlflow

ENV BACKEND_URI postgresql://mlops:mlops@postgres:5432/mlops_db

EXPOSE 5000

CMD mlflow ui --backend-store-uri $BACKEND_URI --host 0.0.0.0
