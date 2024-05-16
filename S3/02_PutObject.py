
import boto3

s3 = boto3.client('s3')

response = s3.put_object(
    Body='',
    Bucket='',
    Key='objectkey',                # File/object name in bucket
)

print(response)

