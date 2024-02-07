import logging

from airflow.decorators import dag, task
from airflow.hooks.base import BaseHook
from airflow.exceptions import AirflowException
from pendulum import datetime

import httpx


logger = logging.getLogger(__file__)


@task
def is_minio_alive():
    logger.info(">> Testing minio connection")
    try:
        connection = BaseHook.get_connection("openminio")
        # url = "http://18.185.135.59:9001/minio/health/live"
        print(connection.host)
        response = httpx.get(url=connection.host)
        if response.status_code != 200:
            logger.error("Problem to connect to minio!")
            raise AirflowException("Problem to connect to minio!")
    except httpx.ConnectError:
        logger.error(f"Invalid url {connection.host}")
        raise AirflowException("Invalid host name.")


@task
def extract_yesterday_data():
    logger.info(">> Extracting yesterday data")
    pass


@task
def create_report(data):
    logger.info(">> Creating report")
    pass


@dag(
    "daily_report",
    description="Daily report about the scrape weather from openweathermap.com",
    schedule="5 0 * * *",
    start_date=datetime(2024, 1, 1, tz="UTC"),
    tags=["weather", "devops", "telekom", "report"],
    catchup=False
)
def main():
    # [ is_minio_alive ] -> [ extract_yesterday_data ] -> [ create_report ]
    data = is_minio_alive() >> extract_yesterday_data()
    create_report(data)
    # pass


main()
