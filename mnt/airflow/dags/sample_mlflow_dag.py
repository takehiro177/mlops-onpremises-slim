from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import os
import glob

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
import catboost as cb
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score

import mlflow
from mlflow.models.signature import infer_signature
mlflow.set_tracking_uri("http://mlflow:5000/")
mlflow.set_experiment("sample_cb_experiment")

DAG_ID = "mlflow_dag"

def load_data():
    data = datasets.load_iris()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    now = datetime.now()
    os.makedirs(f"/opt/airflow/dags/files/{now.strftime('%m-%d-%Y %H:%M:%S')}", exist_ok=True)
    
    X_train.to_csv(f"/opt/airflow/dags/files/{now.strftime('%m-%d-%Y %H:%M:%S')}/X_train.csv", index=False)
    X_test.to_csv(f"/opt/airflow/dags/files/{now.strftime('%m-%d-%Y %H:%M:%S')}/X_test.csv", index=False)
    y_train.to_csv(f"/opt/airflow/dags/files/{now.strftime('%m-%d-%Y %H:%M:%S')}/y_train.csv", index=False)
    y_test.to_csv(f"/opt/airflow/dags/files/{now.strftime('%m-%d-%Y %H:%M:%S')}/y_test.csv", index=False)

def train_model():

    directory = "/opt/airflow/dags/files/*"
    list_of_files = glob.glob(directory)
    latest = max(list_of_files, key=os.path.getctime)
    #n=2
    #nth = sorted(list_of_files, key=os.path.getmtime)[-n]

    import logging

    logging.exception(latest)
    logging.exception(list_of_files)

    X_train = pd.read_csv(latest + "/X_train.csv")
    X_test = pd.read_csv(latest + "/X_test.csv")
    y_train = pd.read_csv(latest + "/y_train.csv")
    y_test = pd.read_csv(latest + "/y_test.csv")
    
    model = cb.CatBoostClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Log the model and the metrics

    with mlflow.start_run():
        mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
        mlflow.log_metric("precision", precision_score(y_test, y_pred, average="macro"))
        mlflow.log_metric("recall", recall_score(y_test, y_pred, average="macro"))
        mlflow.log_metric("f1", f1_score(y_test, y_pred, average="macro"))

        mlflow.sklearn.log_model(model, "sample_cb_model")

        signature = infer_signature(X_train, model.predict(X_train))

        model_info = mlflow.sklearn.log_model(model,
                                              "sample_cb_model",
                                              signature=signature,
                                              input_example=X_train.iloc[:1],
                                              registered_model_name="sample_cb_model"
                                              )  

def load_model():
    model = mlflow.pyfunc.load_model("models:/sample_cb_model/1")
    print(model)

with DAG(
    dag_id=DAG_ID,
    start_date=datetime(2024, 6, 10),
    schedule=None,
    catchup=False,
) as dag:

    load_data_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    train_model_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
    )

    load_model_task = PythonOperator(
        task_id="load_model",
        python_callable=load_model,
    )

    load_data_task >> train_model_task >> load_model_task