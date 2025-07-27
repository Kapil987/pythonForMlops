#### Steps
- Understand the diagram
- Go to aws bedrock > Amazon Bedrock > Model access > Available to request > Request model access
- Go to lambda function > create a lambda function
- lambda function > get familiar with 
Code
Test
Monitor

Aliases
Versions
- Lambda > Configuration> General configuration > timeout > increase to 3 min
- you can change the role also here based on your usecase, the role will have necessary permission for lambda
for simplycity , we need s3fullaccess, cloudwatchfullaccess, bedrockfullaccess

- copy the code from app.py to lambda
- Create an s3 bucket, copy the bucket name and paste in lambda app.py code
- Search for api gateway and click on `create an api` > choose `HTTP API` > build > `API name` > `Review and create` > create
- under `routes` > create > Route and method > POST > /`addthe path` > create
- create integration for your route > Integration target > `lambda function` > create 
- On left side under deploy > stages > create stage as `dev` > then click on deploy by choosing this stage
- copy the url and route in postman, the sample body should be as below


{
    "blog_topic":"india and us relationship"
}