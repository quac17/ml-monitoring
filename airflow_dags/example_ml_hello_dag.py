
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator


def print_hello():
    print("Hello from ML Monitoring Airflow DAG!")


def print_time(**context):
    ts = context["ts"]
    print(f"Execution date: {ts}")


with DAG(
    dag_id="example_ml_hello",
    description="DAG mẫu cho ML Monitoring",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["example", "ml-monitoring"],
) as dag:
    start = EmptyOperator(task_id="start")
    hello = PythonOperator(
        task_id="hello",
        python_callable=print_hello,
    )
    log_time = PythonOperator(
        task_id="log_time",
        python_callable=print_time,
    )
    end = EmptyOperator(task_id="end")

    start >> hello >> log_time >> end
