from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 3, 1, 10, 00),
}

def get_data() -> dict:
    """
    Fetches random user data from an external API.
    
    Returns:
        dict: A dictionary containing user data.
    """
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res: dict) -> dict:
    """
    Formats the raw user data into a structured dictionary.
    
    Args:
        res (dict): Raw user data.
    
    Returns:
        dict: Formatted user data.
    """
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
        f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data() -> None:
    """
    Streams formatted user data to a Kafka topic.
    """
    from kafka import KafkaProducer
    import json
    import time
    import logging

    producer = KafkaProducer(
        bootstrap_servers='broker:29092', max_block_ms=5000)
    curr_time = time.time()
    while True:
        if time.time() > curr_time + 60:  # 1 minute
            break
        try:
            res = get_data()
            data = format_data(res)
            producer.send('user_data', json.dumps(data).encode('utf-8'))
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            continue

# Define the DAG
with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    # Define the task
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data,
    )
