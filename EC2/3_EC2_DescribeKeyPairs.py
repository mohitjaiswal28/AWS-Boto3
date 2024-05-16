
import boto3

ec2 = boto3.client('ec2')

def print_key_pairs():
    # Describe all key pairs
    response = ec2.describe_key_pairs()
    
    for key_pair in response['KeyPairs']:
        print(f"Key Pair Name: {key_pair['KeyName']}")

def main():
    # Print all key pairs
    print_key_pairs()

if __name__ == "__main__":
    main()
