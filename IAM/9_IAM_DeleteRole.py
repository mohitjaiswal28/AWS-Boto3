
import boto3

iam = boto3.client('iam')

response = iam.delete_role(
    RoleName='botoRole-1'
)

print(response)
