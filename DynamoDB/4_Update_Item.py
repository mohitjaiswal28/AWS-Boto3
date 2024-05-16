
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.update_item(
    TableName = 'StudentTable',

    # Column name to be updated
    ExpressionAttributeNames={
        '#C': 'studentName',
    },

    # Value to be updated
    ExpressionAttributeValues={
        ':t': {
            'S': 'JAY',
        }
    },

    # Where to update
    Key={
        'RollNo': {
            'S': '105',
        }
    },

    UpdateExpression='SET #C = :t',
    # UpdateExpression='SET playerName = :t',
)

print(response)