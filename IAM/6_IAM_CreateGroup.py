
import boto3

iam = boto3.client('iam')

response = iam.create_group(
    GroupName='boto-group1'
)

print(response)