### MLOps Interview Questions and Answers 

#### 1. What is MLOps and how is it different from DevOps?
**Answer:**  
MLOps automates the lifecycle of machine learning models—training, deployment, monitoring, and retraining—while DevOps focuses on software development and operational automation for classical apps. MLOps adds data and model management to traditional DevOps.

#### 2. Name some common tools used in MLOps and their purpose.
**Answer:**   
- **MLflow:** Model tracking, experiment management, and deployment  
- **DVC:** Data and model version control  
- **Airflow:** Workflow orchestration and scheduling  
- **Docker:** Containerizing ML applications  
- **Git:** Source code and version control  
- **Dagshub:** Remote repository for code, data, and models in one place.

#### 3. Explain the stages in a typical MLOps pipeline.
**Answer:**  
- Data ingestion and validation  
- Data preprocessing and transformation  
- Model training and experiment tracking  
- Model evaluation and validation  
- Model deployment (to production)  
- Monitoring, logging, and retraining.

#### 4. How do you ensure reproducibility in your ML projects?
**Answer:**  
By using version control for code (Git), data/model versioning tools (DVC), environment tracking (requirements.txt, Docker), and experiment tracking systems (MLflow).

#### 5. What are the typical challenges in deploying machine learning models?
**Answer:**  
- Data and concept drift  
- Dependency management  
- Scalability and latency  
- Model retraining and versioning  
- Ensuring reproducibility and monitoring in production.

#### 6. What’s the role of Docker in MLOps?
**Answer:**  
Docker containers package models and code with dependencies for consistent environment replication across development, test, and production—enabling portable and reliable ML deployments.

#### 7. How do you monitor models in production?
**Answer:**  
By logging performance metrics, tracking input/output data, setting up alerts for data/model drift, and using tools like MLflow, Prometheus, or Grafana to visualize and automate monitoring.

#### 8. Describe a time you built an end-to-end ML workflow.
**Answer:**  
Example: Built a house price prediction system integrating data ingestion (using DVC), preprocessing and model training (logged via MLflow), deployment with Docker, and CI/CD pipelines for regular retraining.

#### 9. What is model versioning and why is it important?
**Answer:**  
Model versioning tracks changes to model files, dependencies, and performance metrics, making it possible to reproduce results, rollback to previous versions, and audit deployments.

#### 10. How do you integrate data versioning in your pipeline?
**Answer:**  
By using DVC or similar tools to track changes in datasets, sync versions with code, and ensure training data matches the deployed models for reliable results.

#### 11. Explain how you use Git and GitHub in MLOps workflows.
**Answer:**  
Git tracks code changes, branches, and collaboration, while GitHub facilitates remote repositories, pull requests, and project management for team-based ML development.

#### 12. How do CI/CD concepts apply to MLOps?
**Answer:**  
CI/CD automates building, testing, and deployment pipelines for models—ensuring regular, automated releases, testing of data/model updates, and rapid rollback if issues arise.

#### 13. What are some best practices for model deployment using Flask?
**Answer:**  
Containerize the Flask app (Docker), use version control, add validation and logging, monitor the API, and automate deployment/integration tests via CI/CD.

#### 14. How would you integrate logging and monitoring into your ML application?
**Answer:**  
Add logging statements at key stages (data, inference, errors), aggregate logs centrally (e.g., with ELK stack), and visualize using platforms like Grafana for continuous monitoring.

#### 15. Can you explain the end-to-end ML workflow using AWS and Sagemaker?
**Answer:**  
Upload data to S3, preprocess using Sagemaker pipelines, train and deploy models on Sagemaker endpoints, use CloudWatch for monitoring, and automate retraining and deployments.


### 16. What is an ML pipeline and why is it important in MLOps?  
**Answer:**  
An ML pipeline automates the sequence of steps—data ingestion, preprocessing, training, evaluation, and deployment—ensuring repeatable, reliable, and efficient workflows.

### 17. How does Data Version Control (DVC) help in collaborative ML projects?  
**Answer:**  
DVC tracks dataset versions alongside code, making it easier for teams to sync, reproduce experiments, and manage large data files without bloating Git repositories.

### 18. What is the difference between batch inference and real-time inference?  
**Answer:**  
Batch inference processes large data sets periodically, while real-time inference provides model predictions on-demand with low latency for immediate decision making.

### 19. Can you explain the concept of model drift and how to handle it?  
**Answer:**  
Model drift refers to degradation in model performance due to changing data distribution over time. It’s handled by continuous monitoring, retraining with fresh data, and validating model outputs.

### 20. How do you manage secret credentials like API keys in your MLOps workflows?  
**Answer:**  
Use secure vault services (AWS Secrets Manager, HashiCorp Vault), environment variables, or encrypted configuration files to avoid hardcoding sensitive information in code.

### 21. What role does Apache Airflow play in MLOps?  
**Answer:**  
Airflow schedules and orchestrates workflows using DAGs, enabling automation of complex ML pipelines such as ETL, training jobs, and deployment workflows.

### 22. What is experiment tracking and why is it important?  
**Answer:**  
Experiment tracking records parameters, metrics, and artifacts of model runs, helping teams compare experiments, reproduce results, and choose the best models for production.

### 23. How do you ensure security and compliance in deployed ML models?  
**Answer:**  
Implement authentication and authorization, encrypt data in transit and at rest, audit logs, apply patch management, and comply with data privacy laws such as GDPR.

### 24. What is feature store and how does it help in MLOps?  
**Answer:**  
A feature store centralizes, manages, and serves features consistently for training and inference, ensuring feature reuse, governance, and reduced data leakage risk.

### 25. Describe how you would containerize an ML model for deployment.  
**Answer:**  
Package the model, dependencies, and inference code into a Docker image, test locally, and deploy the container to a platform such as Kubernetes, Docker Hub, or cloud services.

### 26. What are some common metrics monitored in production ML models?  
**Answer:**  
Accuracy, precision, recall, F1 score, latency, throughput, data drift indicators, and resource utilization (CPU/GPU, memory) are commonly tracked.

### 27. How would you rollback a faulty ML model deployment?  
**Answer:**  
Use model versioning to redeploy the previous stable model, stop or isolate the faulty version, and analyze logs to debug before attempting redeployment.

### 28. What are some ways to optimize model training time in an MLOps pipeline?  
**Answer:**  
Use distributed training, reduce dataset size via sampling, implement early stopping, utilize GPUs/TPUs, and cache processed data or features.

### 29. How does modularity benefit ML workflows?  
**Answer:**  
Modularity enables independent development, testing, and maintenance of pipeline components, leading to easier debugging, reuse, and collaboration.

### 30. Explain the purpose of artifacts in ML workflows.  
**Answer:**  
Artifacts are outputs produced during ML runs—like datasets, models, logs, and metrics—that are stored and tracked for reproducibility and auditing.




## Scenerio based
### 1. Your model’s predictions suddenly become much less accurate after deployment. What steps would you take to diagnose and resolve the issue?
**Answer:**  
Check for data drift or changes in data distribution, review recent code or configuration changes, examine model logs for errors, and compare model input/output samples to pre-production. Retrain the model on new data if necessary.

### 2. You’re asked to build a reproducible ML pipeline for a team project. What approach and tools would you use?
**Answer:**  
Use version control (Git) for code, DVC for data/model versioning, MLflow for experiment tracking, Docker for consistent environments, and workflow orchestrators like Airflow to automate pipeline steps.

### 3. The ML model deployed as an API in Flask is causing latency issues. What do you investigate and how do you mitigate?
**Answer:**  
Profile inference code for bottlenecks, check hardware resources, batch requests where possible, optimize code and dependencies, and consider using a production-ready server (e.g., Gunicorn) or scaling horizontally via containers.

### 4. A teammate accidentally overwrites a dataset in your remote repository. How do you restore the correct version?
**Answer:**  
Revert to the previous dataset version using DVC, sync to remote, and communicate with the team to prevent recurrence by adjusting permissions or workflow.

### 5. Management requests an audit trail for all models deployed in the last 6 months. How would you provide it?
**Answer:**  
Query the model registry (e.g., MLflow Model Registry or Dagshub), export model metadata (versions, deployment times, metrics), and provide logs or dashboards for review.

### 6. You need to ensure that only authorized users can trigger your Airflow ML pipelines. What do you implement?
**Answer:**  
Set up authentication and role-based access control (RBAC) in Airflow, integrate with the company’s identity provider if possible, and audit access logs regularly.

### 7. During retraining, your pipeline fails at the data validation stage. What should you check?
**Answer:**  
Inspect schema mismatches, null or unexpected values, upstream data source changes, and review validation scripts for outdated or brittle logic.

### 8. You’re tasked with deploying a model to AWS Sagemaker. What are the key steps?
**Answer:**  
Upload data to S3, train the model using Sagemaker training jobs, register the trained model, deploy it to an endpoint, and configure monitoring/alarms.

### 9. Stakeholders want a rollback strategy for new model deployments. How do you enable this?
**Answer:**  
Maintain versioned model artifacts, deploy using a blue-green or canary approach, and automate rollback to a previous version when metrics or health checks trigger alerts.

### 10. Your team wants to scale up model training using cloud GPUs. What do you consider?
**Answer:**  
Profile resource needs, select appropriate GPU instances, manage costs with spot/reserved instances, distribute training if possible, and automate resource teardown post-training.

### 11. After integrating a 3rd-party API into your ETL pipeline, failures increase. How do you improve reliability?
**Answer:**  
Implement error handling and retries, log failures with context, monitor API health, set up alerts, and use circuit breakers or fallback mechanisms if the API is unavailable.

### 12. New regulations require that all ML predictions are explainable. What changes would you make?
**Answer:**  
Integrate explainability tools (like SHAP or LIME), log explanations alongside predictions, update documentation, and add endpoints or UI features to deliver explanations.

### 13. You discover model input data is leaking target values (label leakage). What corrective actions do you take?
**Answer:**  
Audit data pipelines for leakage sources, redesign feature engineering to prevent leakage, retrain models, and update validation to catch future occurrences.

### 14. Monitoring shows that model accuracy is dropping gradually post-deployment. What’s your long-term strategy?
**Answer:**  
Automate periodic retraining using new data, monitor drift, implement continuous evaluation, and schedule regular reviews of model performance and data quality.

### 15. You must synchronize and version both large datasets and code across multiple teams. What is your approach?
**Answer:**  
Use DVC or similar for data versioning, Git for code, ensure data/code version alignment in pipeline configurations, and enforce protocols for remote sync and access control.


### Conceptual & Technical Questions

1. **How do you implement CI/CD for ML models?**  
Establish pipelines to automate data validation, model training, testing, and deployment using tools such as Jenkins, GitLab CI, or Azure DevOps tailored for ML workflows.

2. **What is hyperparameter tuning and how do you automate it?**  
Hyperparameter tuning finds optimal parameters for a model. Tools like Optuna, Hyperopt, and cloud platforms can automate this process.

3. **Describe model registry and its use.**  
A model registry is a repository to store and manage different model versions, facilitating deployment, rollback, and audit trails.

4. **How do you make ML pipelines portable across environments?**  
Use containerization (Docker), infrastructure as code, and environment management (virtualenv, Conda) to ensure environment consistency.

5. **Explain canary and blue-green deployment strategies in MLOps.**  
Canary gradually shifts traffic to new models for safety. Blue-green maintains two environments, switching traffic when ready, allowing quick rollbacks.

6. **What is the role of feature engineering in the ML workflow?**  
Transforms raw data into features improving model performance, requiring careful pipeline design for automation and reproducibility.

7. **Name some tools used for orchestration in MLOps.**  
Apache Airflow, Kubeflow, and Prefect are commonly used for scheduling and orchestrating complex workflows.

8. **Describe how to monitor data quality in production ML.**  
Monitor for schema drift, missing values, and out-of-range features using logging, validation frameworks, and alerting.

9. **What are the risks of untracked machine learning experiments?**  
Lack of reproducibility, difficulty debugging, and inability to prove model lineage or regulatory compliance.

10. **How do you ensure data privacy in ML projects?**  
Apply encryption, anonymization, access controls, and consider privacy-by-design principles.

11. **Distinguish between data drift and concept drift.**  
Data drift is a change in input data distribution; concept drift is a change in the relationship between input and target.

12. **How do you ensure secure ML model hosting?**  
Harden APIs, manage secrets, limit access, and enable secure logging and monitoring.

13. **What is model explainability and why does it matter?**  
Explainability tools (like SHAP, LIME) reveal how features influence predictions, supporting transparency, trust, and compliance.

14. **What does A/B testing mean in ML model deployment?**  
It means serving multiple model versions to subsets of the population and comparing their performance statistically.

15. **How do you productionize a Jupyter notebook ML prototype?**  
Refactor code into modules or scripts, add error handling, input validation, and test before deploying via CI/CD.

### Scenario-Based & Practical Questions

16. **You’ve just found labels are imbalanced—how do you proceed?**  
Resample data (e.g., SMOTE), try stratified folds, use metrics suitable for imbalance (AUC/ROC), and document in pipeline.

17. **A new data pipeline integration consistently fails at night—what’s your debugging approach?**  
Check logs and job scheduler config, resource bottlenecks, and data source availability at night before implementing alerts.

18. **A model intermittently fails with memory errors during training—how do you resolve?**  
Profile memory usage, optimize data loading, sample batches, and, if possible, move to larger or cloud-based machines.

19. **You need to deploy a model as a REST API with auto-scaling. Describe your approach.**  
Containerize with Docker, use Gunicorn or FastAPI, deploy on Kubernetes or AWS ECS with load balancer and autoscaler rules.

20. **A data scientist wants to run large-scale experiments but lacks GPU access. What do you do?**  
Provision cloud GPU resources, set up necessary permissions/budgets, and integrate resource management with orchestration tools.

21. **A model predicting rare events underperforms; what actions do you take?**  
Investigate labeling, resample or aggregate rare class data, try different loss functions or ensemble approaches.

22. **Stakeholders need auditability for all model changes—how do you enable it?**  
Integrate code/data versioning, detailed logging, and model registry use so all changes are tracked and reproducible.

23. **You are to refactor a pipeline suffering from ‘spaghetti code.’ What strategy will you use?**  
Modularize processes, enforce code standards, document pipeline steps, and apply version control best practices.

24. **Your team wants to apply DVC to an existing project—where do you start?**  
Track current datasets and models with DVC add, adjust pipeline to use DVC stages, and ensure remote storage for collaboration.

25. **How do you manage dependency conflicts in ML environments?**  
Containerize with Docker, pin dependencies, and use tools like pip-compile or conda-lock to freeze environments.

26. **Model performance metrics drop only for one specific region. How do you approach the issue?**  
Analyze data distribution for that region, check for unrepresented features, possible data quality issues, then consider region-specific retraining.

27. **You’re asked to set up automated retraining on new data arrivals. What tools and logic would you use?**  
Use Airflow to schedule retraining on new data detection, update model registry, and alert on model validation failures.

28. **A third-party package your solution depends on becomes deprecated. What is your workflow?**  
Audit dependencies, validate upgrade paths or alternatives, test integration extensively in staging, and roll out updates with version control.

29. **Stakeholders want end-to-end pipeline run reports. How do you automate this?**  
Integrate reporting scripts in the workflow manager; schedule email/Slack notifications with logs and summarized metrics on each pipeline run.

30. **A custom model is slow to load during API cold-start. What optimizations do you consider?**  
Serialize with ONNX or joblib, use model “warmers,” lazy-load heavy dependencies, or maintain warm standby endpoints.

### Knowledge & Applied Skills

31. **Which cloud services have you used for end-to-end MLOps?**  
AWS Sagemaker, Google Vertex AI, Azure ML; each offers tools for pipeline orchestration, deployment, and experiment tracking.

32. **What is a pipeline DAG and why is it useful in Airflow?**  
A DAG (Directed Acyclic Graph) defines task dependencies and order, ensuring correct and reliable execution flow.

33. **How do you manage shared feature definitions across teams?**  
Centralize definitions in a feature store with documented access, validation, and governance.

34. **What’s the purpose of model “shadow mode” deployment?**  
Runs models in parallel on live data without affecting users, to compare predictions and monitor performance risk-free.

35. **Explain the use of Prometheus and Grafana in MLOps.**  
Prometheus collects and stores metrics; Grafana visualizes them for monitoring model/API/system health.

36. **How would you scale a model that is used for both batch and real-time inference?**  
Deploy separate services or endpoints optimized for each scenario—batch for throughput, real-time for latency and concurrency.

37. **How do you validate input data at inference time in production?**  
Apply runtime checks—type, range, schema validators—raise informative errors, and log anomalies for analysis.

38. **Name techniques to reduce inference latency.**  
Model compression, quantization, optimized serving frameworks (TensorFlow Serving), and hardware accelerators.

39. **How do you separate model configuration from code?**  
Store configs in YAML, JSON, or environment variables and parse them at runtime for flexibility.

40. **What are the pros and cons of serverless ML deployment?**  
Pros: easy scaling, lower ops burden. Cons: cold-start latency, resource limits, challenging to persist state.

### Advanced & Troubleshooting

41. **Describe the security implications of model exposure via API.**  
Risk of data leakage, reverse engineering; mitigate with authentication, usage monitoring, and data redaction.

42. **How would you automate drift detection and alerting?**  
Build pipelines to monitor performance and data distribution KPIs, alert on thresholds, and trigger retraining as needed.

43. **Your orchestrator fails intermittently and some jobs are missed. How do you prevent data loss?**  
Implement job status tracking, retries, idempotent processing, and persistent checkpoints.

44. **A user reports predictions that violate known business logic. How do you trace and resolve the root cause?**  
Audit input/output data, verify pipeline transformations and model logic, check feature leakage or data corruption.

45. **How do you manage cost when running large ML workflows in the cloud?**  
Use resource quotas, auto-scaling, monitor resource usage, schedule shutdowns for idle resources, and prefer spot/preemptible VMs as appropriate.

46. **Describe the process of rolling out a critical patch in a production MLOps pipeline.**  
Test in staging, create a canary deployment, monitor closely, and roll back on any failures—with proper notification.

47. **An upstream breaking data schema change is expected—what’s your plan of action?**  
Coordinate with data owners, add backward-compatible parsers, update validation and transformation steps, and run tests in staging.

48. **How do you keep model documentation up to date and accessible?**  
Automate documentation from tracking tools, maintain README/CONTRIBUTING docs in source control, and use wikis or dashboards.

49. **Explain version pinning and its role in reproducibility.**  
Specifying exact dependency versions for all environments ensures that code and models behave identically regardless of where run.

50. **You need to migrate an on-prem MLOps pipeline to the cloud. What are the main steps?**  
Inventory all components, evaluate cloud equivalents, migrate data/models, update integrations, thoroughly test, then decommission on-prem resources.



## Python Questions and Answers

1. **What is the difference between a list and a tuple in Python?**  
   *Lists are mutable and can be changed after creation, while tuples are immutable and cannot be changed once created.*

2. **What is PEP 8 and why is it important?**  
   *PEP 8 is a style guide for Python code that helps ensure code readability and consistency across the Python community.*

3. **Explain list comprehensions with an example.**  
   *List comprehensions provide a concise way to create lists. Example: `[x*x for x in range(5)]` results in `[0, 1, 4,[7]`.*

4. **How do you handle exceptions in Python?**  
   *Using try/except blocks. Example:*
   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero")
   ```

5. **What is a decorator in Python?**  
   *A decorator is a function that takes another function as input and extends its behavior without directly modifying it, often via the @ syntax.*

6. **Explain the difference between deep copy and shallow copy.**  
   *Shallow copy copies references to objects, while deep copy creates copies of the objects themselves.*

7. **What is a lambda function?**  
   *A lambda is an anonymous function defined with the `lambda` keyword, typically used for small operations.*

8. **How do you merge two dictionaries in Python 3.5+?**  
   *Use the `{**dict1, **dict2}` syntax or the merge `|` operator in Python 3.9+.*

9. **What are generators and how do you create one?**  
   *Generators use the `yield` statement to produce a sequence of values lazily. Example:*
   ```python
   def gen_nums():
       yield 1
       yield 2
   ```

10. **Explain the difference between `@classmethod` and `@staticmethod`.**  
    *`@classmethod` receives the class as the first argument, `@staticmethod` does not receive any implicit arguments.*

11. **What is the Global Interpreter Lock (GIL)?**  
    *The GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time, limiting concurrency.*

12. **How do you reverse a string in Python, without using built-in functions?**  
    *Using slicing: `reversed_str = s[::-1]`.*

13. **What is the purpose of the `with` statement?**  
    *It simplifies exception handling by encapsulating setup and teardown code, commonly used with file operations.*

14. **How do you create a virtual environment in Python?**  
    *Using `python -m venv env` and activate with the corresponding script for your OS.*

15. **Explain the use of `__init__` in Python classes.**  
    *`__init__` is the constructor method called when a new instance is created.*

16. **What are iterators and how are they different from iterables?**  
    *An iterable can be looped over (like lists), whereas an iterator is an object with `__next__()` and `__iter__()` methods.*

17. **Describe slicing in Python.**  
    *Slicing allows extraction of a subsequence using the `[start:stop:step]` syntax.*

18. **How is memory managed in Python?**  
    *Memory management is handled via reference counting and garbage collection.*

19. **What is monkey patching?**  
    *Monkey patching refers to runtime modifications of a class or module, often used for testing.*

20. **Explain the difference between `append()` and `extend()` methods of list.**  
    *`append()` adds a single element to the end, while `extend()` adds elements from another iterable.*

21. **How do you read and write files in Python?**  
    *Using `open()` with the desired mode, e.g., `with open('file.txt', 'r') as f:`.*

22. **What is the difference between `is` and `==` in Python?**  
    *`is` checks for object identity, `==` checks for value equality.*

23. **How do you handle circular imports in Python?**  
    *By reorganizing imports or using local imports inside functions.*

24. **Explain Python’s garbage collection.**  
    *Python uses reference counting and a cyclic garbage collector to clean up unused objects in memory.*

25. **What are context managers? How do you create a custom one?**  
    *Context managers define runtime context via `__enter__` and `__exit__` methods. Use the `with` statement or the `contextlib` module to create custom ones.*

## Flask Questions and Answers

26. **What is Flask? Why is it called a micro-framework?**  
    *Flask is a lightweight web framework for Python. It's called a micro-framework because it does not include built-in tools like form validation or database abstraction, allowing developers to add only what they need.*

27. **How do you create a basic route in Flask?**  
    *By using the `@app.route()` decorator:*
    ```python
    @app.route('/')
    def home():
        return "Hello, Flask!"
    ```

28. **What is a Flask extension? Name some useful ones.**  
    *Extensions add functionality to Flask. Examples: Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-Migrate.*

29. **How do you manage sessions in Flask?**  
    *By default, Flask uses secure cookies for sessions, accessible via `flask.session`.*

30. **How do you connect Flask to a database?**  
    *Use an extension like Flask-SQLAlchemy for relational databases, or Flask-MongoEngine for MongoDB. Configure the URI, instantiate the extension, and define your models.*

31. **What template engine does Flask use by default?**  
    *Flask uses Jinja2 as its template engine.*

32. **How do you return JSON data from a Flask route?**  
    *Use `flask.jsonify` to generate a proper JSON response:*
    ```python
    from flask import jsonify
    @app.route('/api')
    def api():
        return jsonify({'key':'value'})
    ```

33. **What are Flask blueprints?**  
    *Blueprints let you organize a Flask app into reusable components (modules), with routes, templates, etc.*

34. **How do you implement forms in Flask?**  
    *Either handle HTML forms manually or use the Flask-WTF extension for form handling and CSRF protection.*

35. **How do you enable debugging in Flask?**  
    *Set `app.debug = True` or run with the FLASK_DEBUG environment variable set to 1.*

36. **Explain Flask’s request and response objects.**  
    *The `request` object contains all incoming request data; the `response` object is the output sent to the client.*

37. **How do you implement authentication in Flask?**  
    *Use Flask-Login extension for session management, or Flask-JWT for token-based auth.*

38. **What is the purpose of `flask.g`?**  
    *It is a global namespace for holding data during a single application context (like DB connections per request).*

39. **How do you handle static files in Flask?**  
    *Flask serves static files from the `static/` folder by default at the `/static/` route.*

40. **How can you run background tasks in Flask?**  
    *Use task queues like Celery or RQ with a broker such as Redis for running tasks in the background.*

41. **How do you handle errors in Flask?**  
    *Define error handlers using `@app.errorhandler`. Example:*
    ```python
    @app.errorhandler(404)
    def not_found(e):
        return "Page not found", 404
    ```

42. **Explain Flask’s application context and request context.**  
    *The application context (`app.app_context()`) holds global app data, and the request context (`app.test_request_context()`) holds data specific to the current request.*

43. **Describe the steps in deploying a Flask app to production.**  
    *Use a production-ready WSGI server (like Gunicorn or uWSGI), configure for security, and use a reverse proxy (like Nginx).*
44. **What’s the difference between Flask and Django?**  
    *Flask is minimalistic and flexible, while Django is a full-stack framework with lots of built-in features.*

45. **How do you write unit tests for Flask apps?**  
    *Use the built-in `unittest` module or Pytest. Use the test client (`app.test_client()`) to simulate requests.*

46. **What are Flask hooks?**  
    *Special functions like `before_request`, `after_request`, `teardown_request`, used to inject code at different stages of request processing.*

47. **How do you add CORS headers in a Flask API?**  
    *Use the Flask-CORS extension to manage Cross-Origin Resource Sharing headers.*

48. **How can you secure user passwords in a Flask app?**  
    *Hash passwords with a library like bcrypt or Flask-Bcrypt before storing them in the database.*

49. **What is Flask-Migrate, and how is it used?**  
    *It provides database schema migration support, built on top of Alembic and Flask-SQLAlchemy.*

50. **How do you make RESTful APIs with Flask?**  
    *By creating resource-based routes and using methods (GET, POST, PUT, DELETE), often assisted by Flask-RESTful.*