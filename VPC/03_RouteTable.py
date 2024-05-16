
import boto3

vpc = boto3.client('ec2')

# Creating Route table
response1 = vpc.create_route_table(
    VpcId='',
    TagSpecifications=[
        {
            'ResourceType': 'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Route table 1'
                },
            ]
        },
    ]
)

print(response1)
rtid = response1['RouteTable']['RouteTableId']
print(rtid)


# Associate Route table
response2 = vpc.associate_route_table(
    RouteTableId=rtid,
    SubnetId='',
)

print(response2)