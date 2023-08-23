from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python import PythonOperator

with DAG(
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 0,
        "retry_delay": timedelta(seconds=60),
        "start_date": datetime(2021, 1, 1),
    },
    schedule_interval=None,
    dag_id="seed_data_check_sans_dbt",
    description="A dag to check the integrity of imported data",
    tags=["test"],
) as dag:
    t1 = PostgresOperator(
        task_id="titanic-check",
        sql="./sql/query-titanic.sql",
        postgres_conn_id="example_db",
    )
    def print_sql_results(**kwargs):
        ti = kwargs['ti']
        result = ti.xcom_pull(task_ids='titanic-check')
        print(f"Result: \n{result}")
        return 
    t2 = PythonOperator(
        task_id="print-check-result",
        python_callable=print_sql_results,
    )
    #Set dependencies
    t1 >> t2
