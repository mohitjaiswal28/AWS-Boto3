
import boto3

ec2 = boto3.client('ec2')

def create_security_group(group_name, description, vpc_id):
    # Create the security group
    response = ec2.create_security_group(
        GroupName=group_name,
        Description=description,
        VpcId=vpc_id
    )
    
    group_id = response['GroupId']
    print(f"Security group '{group_name}' created with ID: {group_id}")
    
    return group_id

def main():
    # Specify the parameters for the new security group
    group_name = 'MyBoto3SecurityGroup'
    description = 'My security group created with Boto3'
    vpc_id = ''  # Specify your VPC ID
    
    # Create the security group
    group_id = create_security_group(group_name, description, vpc_id)

if __name__ == "__main__":
    main()
