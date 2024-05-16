
import boto3

iam = boto3.client('iam')

response = iam.list_groups()

for group in response['Groups']:
    print(group['GroupName'])