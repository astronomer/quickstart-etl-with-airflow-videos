from datetime import datetime

from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator




@dag(
    start_date=datetime(2024, 10, 18),
    schedule="@daily",
    catchup=False,
    template_searchpath=["include"],
)
def my_etl_dag():


my_etl_dag()
