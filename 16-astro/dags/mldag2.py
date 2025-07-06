from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.decorators import dag # Import the dag decorator

## Define our task 1
def preprocess_data():
    print("Preprocessing data...")

## Define our task 2
def train_model():
    print("Training model...")

## Define our task 3
def evaluate_model():
    print("Evaluate Models...")

# Define the DAG using the decorator
@dag(
    dag_id='ml_pipeline',
    start_date=datetime(2025, 7, 7),
    schedule='@daily',
    catchup=False,
    default_args={'owner': 'airflow', 'retries': 1},
)
def ml_pipeline_dag(): # Define a function for your DAG
    ## Define the tasks inside the function
    preprocess = PythonOperator(task_id="preprocess_task", python_callable=preprocess_data)
    train = PythonOperator(task_id="train_task", python_callable=train_model)
    evaluate = PythonOperator(task_id="evaluate_task", python_callable=evaluate_model)

    ## Set dependencies inside the function
    preprocess >> train >> evaluate

ml_pipeline_dag() # Call the function to instantiate the DAG