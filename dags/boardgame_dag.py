
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
default_args = {
        'owner': 'airflow',
        'start_date': datetime(2019, 9, 25)
        }
dag = DAG('bgg_crawler', default_args=default_args, schedule_interval='0 * * * *', catchup=False)
t1 = BashOperator(
    task_id='schedule_bgg_crawler',
    bash_command="cd /Users/willshin/Development/ScrapyAndAirflow_BoardGame/BGGDataScraping && scrapy crawl bgg -o file_'{{ execution_date }}'.csv -t csv",
    dag=dag)
