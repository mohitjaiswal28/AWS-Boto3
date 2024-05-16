
import boto3

iam = boto3.client('iam')

response = iam.add_user_to_group(
    GroupName='boto-group1',
    UserName='boto3user1'
)

print(response)