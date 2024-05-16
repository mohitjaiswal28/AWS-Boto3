
import boto3

iam = boto3.client('iam')

response = iam.attach_group_policy(
    GroupName='boto-group1',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)

print(response)