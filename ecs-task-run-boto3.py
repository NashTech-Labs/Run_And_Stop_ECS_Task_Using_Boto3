import boto3
import json

client = boto3.client("ecs", region_name="us-east-1")

ec2 = boto3.resource('ec2')

response = client.run_task(
    taskDefinition='console-sample-app',
    launchType='FARGATE',
    cluster='default',
    platformVersion='LATEST',
    count=1,
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-9e7c0fc1',
            ],
            'assignPublicIp': 'ENABLED',
            'securityGroups': ["sg-0bfa5becbde957cd3"]
        }
    }
)

print(json.dumps(response, indent=4, default=str))