
import boto3

s3 = boto3.client('s3')

response = s3.put_bucket_versioning(
    Bucket='',
    VersioningConfiguration={
        'Status': 'Enabled'
        # 'Status': 'Disabled'
    }
)