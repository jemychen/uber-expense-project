import logging
import datetime

# Airflow is an open-source management platform
from airflow import DAG # DAG is a Directed Acyclic Graph

dag = DAG (
    'uber_tracking',
    description = 'Tracking expenses via Uber',
    start_date = datetime.datetime.now(),
    schedule_interval = '@weekly',
    tags = ['UBER']
)