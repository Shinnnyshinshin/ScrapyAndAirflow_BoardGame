# ScrapyAndAirflow_BoardGame

This project describes an initial exploration of the potential of Apache Airflow, a workflow management system developed by Airbnb.  In a simple test case it will be used to write a ETL pipeline for extracting data from a set of webpages every hour. Scrapy, a python framework will be used to do the actual web crawling and data scraping. 

## Creating the scrapy project and item schema
When the scrapy project is created it should have automatically created some files. One is items.py, which is used to describe a Python class that the results will be stored in. 

### items.py
```python
from scrapy.item import Item, Field
class BggdatascrapingItem(Item):
    title = Field()
    rank = Field()
    release_date = Field()
    geek_rating = Field()
    avg_rating = Field()
    num_voters = Field()
    url = Field()
```

### bgg_spider.py

This is a file that is under BGGDataScraping/spiders. It contains the class that will describe the actual parser, and the function is iterating through the first 50 pages and parsing each game into an item, which includes the fields we are interested in like rank, average rating and title.

## Scheduling the web crawling using Apache Airflow

The next step is to use Apache Airflow to schedule a webcrawl every hour. The following code is included in the Airflow DAG.

```python
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
default_args = {
        'owner': 'airflow',
        'start_date': datetime(2019, 6, 15)
        }
dag = DAG('bgg_crawler', default_args=default_args, schedule_interval='0 * * * *', catchup=False)
t1 = BashOperator(
    task_id='schedule_bgg_crawler',
    bash_command="cd ~/BGGDataScraping && scrapy crawl bgg -o file_'{{ execution_date }}'.csv -t csv",
    dag=dag)
```

Once the process is complete, the output is written to a series of CSVs.
