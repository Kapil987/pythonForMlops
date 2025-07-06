### astronomer.io
This project sets up an **Airflow ETL pipeline** to pull data from **NASA's APOD API**, transform it, and load it into a **PostgreSQL database**. It uses **Docker** to containerize Airflow and Postgres, ensuring a consistent environment. The workflow involves an **Extract** task (using `SimpleHttpOperator`), a **Transform** task (using Airflow's TaskFlow API), and a **Load** task (using `PostgresHook`) to store the processed astronomy data.

Prequisite: docker on the sytem
vscode remote ssh config file
```bash
Host 34.238.39.221
  HostName 34.238.39.221
  User ubuntu
  IdentityFile  C:\Users\karan\Downloads\aws\aws4-nvirginia.pem
```

1) Install astro cli on windows
https://www.astronomer.io/docs/astro/cli/get-started-cli?tab=windows#install-the-astro-cli 
OR on linux
https://www.astronomer.io/docs/astro/cli/install-cli/?tab=linux#install-the-astro-cli
curl -sSL install.astronomer.io | sudo bash -s
The instance should be min t3.medium
NOte: allow port 8080 in your instance security group

2) sign up to astronomer cloud
3) Once initial setting up and login into astro account you will be asked as `Deploy your first Astro project`
choose aws and click on `Create Deploymnet in Astro`

4) `astro dev init` # initialises empty astro project on your system
5) `astro dev start` #build the project and make airflow run on ip:8080 by default
for local system it will work
for cloud we need to proxy pass using ngix
default creds are `admin` and `admin`




6) click on dags and you will see the `example_astronauts` is deployed on the airflow, trigger this dag and if you click on the bar symbol you will see the task and status if you click below it it will show the logs
Explore the options and UI, like evenlogs, details, graph,xcom (passing values) etc
7) To stop the ui use `astro dev stop`

#### Creating you first DAG
1) create a new file in dags folder as mldag.py once done do `astro dev stop`
then `astro dev start`
debug command
```bash
astro dev run dags list-import-errors
```
2) observe the logs in airflow UI

#### Getting Familiar with Taskflow API in Airflow

A practical use case for this exact TaskFlow API approach in an IT job, particularly in **Data Engineering** or **MLOps**, would be a **sequential data transformation and feature engineering pipeline**.

### Use Case: Customer Lifetime Value (CLTV) Feature Generation 📊
Customer Lifetime Value (CLTV) is a prediction of the total revenue a business expects to earn from a customer over their entire relationship

Imagine your IT team needs to calculate an updated Customer Lifetime Value (CLTV) score daily for marketing and sales.

* **`start_number()`** could represent **extracting raw sales data** for a customer base.
* **`add_five()`** could be **aggregating historical purchases** to get total revenue per customer.
* **`multiply_by_two()`** might **apply a growth factor** based on recent trends or a specific business rule.
* **`subtract_three()`** could represent **deducting customer churn probability** or subscription cancellation rates.
* **`square_number()`** might be a final **normalization or transformation step** to scale the CLTV score for a machine learning model or reporting.

