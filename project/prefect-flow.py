import os
import time
from prefect import Flow, task
from scripts.utils import write_csv, load_to_postgres

@task
def fetch():
    write_csv()

@task
def load():
    load_to_postgres()

@task
def run_dbt():
    os.system("docker-compose run dbt dbt run")

with Flow("BRT Real-Time Pipeline") as flow:
    fetch()
    load()
    run_dbt()

if __name__ == "__main__":
    while True:
        flow.run()
        time.sleep(60)
