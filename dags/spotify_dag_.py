from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from spotify_etl_ import run_spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag_',
    default_args=default_args,
    description='Spotify ETL',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='ellens_spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag,
)

run_etl
