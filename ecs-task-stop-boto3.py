import boto3
import json

client = boto3.client("ecs", region_name="us-east-1")

paginator = client.get_paginator('list_tasks')

response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
    }
)

for each_page in response_iterator:
    for each_task in each_page['taskArns']:
        response = client.stop_task(task=each_task)
        print(json.dumps(response, indent=4, default=str))