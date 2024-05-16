
import boto3

ec2 = boto3.client('ec2')

def add_inbound_rules(group_id):
    # Add inbound rules to allow traffic on ports 22 (SSH) and 80 (HTTP)
    ec2.authorize_security_group_ingress(
        GroupId=group_id,
        IpProtocol='tcp',
        FromPort=22,
        ToPort=22,
        CidrIp='0.0.0.0/0'  # Allow traffic from all IPv4 addresses
    )

def main():
    group_id=''
    add_inbound_rules(group_id)
    print("Done!")

if __name__ == "__main__":
    main()
  