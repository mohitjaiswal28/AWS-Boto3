
import boto3

ec2 = boto3.client('ec2')

def create_key_pairs():
    # Describe all key pairs
    mykey=ec2.create_key_pair(KeyName='MohitKey1')
    print("Key pair created")

    print(type(mykey))
    key_name = mykey['KeyName']
    print(f"KeyName: {key_name}")

def main():
    create_key_pairs()

if __name__ == "__main__":
    main()
