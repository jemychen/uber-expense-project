import logging
import datetime

# Airflow is an open-source management platform
from airflow import DAG # DAG is a Directed Acyclic Graph

# Import variable and Connection
from airflow.models import Variable
from airflow.models.connection import Connection

# Import PostgresHook
from airflow.hooks.postgres_hook

dag = DAG (
    'uber_tracking',
    description = 'Tracking expenses via Uber',
    start_date = datetime.datetime.now(),
    schedule_interval = '@weekly',
    tags = ['UBER']
)

def fixing_location():
    redshift_hook = PostgresHook("redshift")
    sql_stmt = sql_statements.fixing_locations
    redshift_hook.run(sql_stmt)
    print(f"Locations fixed successfully.")

