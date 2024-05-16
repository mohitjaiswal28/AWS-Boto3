
import boto3

s3 = boto3.client('s3')

# 1. List buckets
response1 = s3.list_buckets()
for bucket in response1['Buckets']:
    print(bucket['Name'])

# 2. Create bucket
bucket_name = ''
region = 'ap-south-1'  
location_constraint = {'LocationConstraint': region}

# Create the bucket with region specified
response2 = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location_constraint
)

print(response2)