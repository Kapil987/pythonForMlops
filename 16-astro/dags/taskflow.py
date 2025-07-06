"""
Airflow's TaskFlow API, featuring decorators like `@task`, offers a streamlined and more 
Pythonic approach to defining tasks. 
This eliminates the need for explicit operator instantiations (e.g., `PythonOperator`), 
making your DAG code cleaner and more intuitive. Let's see how to refactor the prior example using the 
`@task` decorator.
"""

from airflow import DAG
from airflow.decorators import task
from datetime import datetime

## Define the DAG

with DAG(
    dag_id='calculate_customer_Lifetime_value',
    start_date=datetime(2023,1,1),
    schedule='@once',
    catchup=False,
) as dag:
    

    # Task 1: Start With the initial number
    @task
    def extracting_raw_sales_data():
        initial_value=10
        print(f"Extracting raw sales data : {initial_value}")
        return initial_value
    
    # Task 2: Add 5 to the number
    @task
    def aggregating_historical_purchases(number):
        new_value = number + 5
        print(f"Aggregating historical purchases, so Adding 5: {number} + 5 = {new_value}")
        return new_value
    
    # Task 3: Multiply by 2
    @task
    def multiply_by_growth_factor(number):
        new_value = number * 2
        print(f"Apply a growth factor,so Multiply by 2: {number} * 2 = {new_value}")
        return new_value
    
     # Task 4: Subtract 3
    @task
    def subscription_cancellations(number):
        new_value = number - 3
        print(f"Subtract 3: {number} - 3 = {new_value}")
        return new_value
    
    # Task 5: Square the number
    @task
    def normalization(number):
        new_value = number ** 2
        print(f"Square the result: {number}^2 = {new_value}")
        return new_value
    
    ## Set task dependencies
    start_value=extracting_raw_sales_data()
    added_values=aggregating_historical_purchases(start_value)
    multiplied_value=multiply_by_growth_factor(added_values)
    subtracted_value=subscription_cancellations(multiplied_value)
    square_value=normalization(subtracted_value)
