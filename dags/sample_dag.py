# dags/sample_dag.py

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_hello():
    print("Hello Satish  reddy")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}



with DAG(
    dag_id='sample_dag',
    default_args=default_args,
    description='A simple DAG to demonstrate structure',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:
    
    hello_task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    hello_task




