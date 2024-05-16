
import boto3

s3 = boto3.client('s3')

def delete_object_permanently(bucket_name, key):
    # List all versions of the object
    response = s3.list_object_versions(Bucket=bucket_name, Prefix=key)

    # Delete all versions of the object, including delete markers
    for version in response.get('Versions', []):
        s3.delete_object(
            Bucket=bucket_name,
            Key=key,
            VersionId=version['VersionId']
        )
    
    # Also delete any delete markers
    for marker in response.get('DeleteMarkers', []):
        s3.delete_object(
            Bucket=bucket_name,
            Key=key,
            VersionId=marker['VersionId']
        )

    print(f"Object '{key}' deleted permanently from bucket '{bucket_name}'.")

def main():
    # Specify the bucket name and key of the object you want to delete
    bucket_name = ''
    key = 'objectkey'

    # Delete the object permanently
    delete_object_permanently(bucket_name, key)

if __name__ == "__main__":
    main()