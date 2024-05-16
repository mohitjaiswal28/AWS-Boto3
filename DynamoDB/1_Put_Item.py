
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
        'RollNo': {
            'S': '105',
        },
        'studentName': {
            'S': 'Mohit',
        }
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='StudentTable',
)

print(response)