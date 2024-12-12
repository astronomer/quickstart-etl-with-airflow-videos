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

    @task
    def extract():
        import requests

        lat = 38.4937
        lon = 14.9272

        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=sunset&timezone=auto&forecast_days=1"
        )

        return response.json()

    @task
    def transform(api_response):
        transformed_data = {
            "date": api_response["daily"]["time"][0],
            "latitude": api_response["latitude"],
            "longitude": api_response["longitude"],
            "sunset": api_response["daily"]["sunset"][0],
        }

        return transformed_data


    _extract = extract()
    _transform = transform(api_response=_extract)



my_etl_dag()
