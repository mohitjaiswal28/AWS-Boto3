
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_item(
    Key={
        'playerId': {
            'N': '103',
        },
        'playerName': {
            'S': 'Jay Shenkar',
        }
    },
    TableName='PlayersTable',
)

print(response)