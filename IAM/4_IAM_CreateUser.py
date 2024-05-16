
import boto3

iam = boto3.client('iam')

response = iam.create_user(
    UserName='boto3user1',
    Tags=[
        {
            'Key': 'Department',
            'Value': 'DevSecOpsEngineers'
        },
    ]
)