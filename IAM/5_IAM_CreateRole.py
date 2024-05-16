
import boto3

iam = boto3.client('iam')

response = iam.create_role(
    RoleName='botoRole-1',
    AssumeRolePolicyDocument='{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": {"Service": "ec2.amazonaws.com"}, "Action": "sts:AssumeRole"}]}',
    Description='Role desc ',
    MaxSessionDuration=3600,
    PermissionsBoundary='arn:aws:iam::aws:policy/AdministratorAccess',
    Tags=[
        {
            'Key': 'Dept',
            'Value': 'Testing'
        },
    ]
)

print(response)
