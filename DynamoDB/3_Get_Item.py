
import boto3;

dynamodb = boto3.client('dynamodb')

response = dynamodb.get_item(
    Key={
        'RollNo': {
            'S': '105',
        },
    },
    TableName='StudentTable',
)

print(response)


# # Full table
# response = dynamodb.scan(
#     TableName = 'StudentTable'
# )

# print(response)