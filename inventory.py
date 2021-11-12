import boto3

## ref https://stackoverflow.com/questions/66085408/how-generate-ec2-inventory-from-multiple-aws-account-using-python-boto3

session = boto3.Session()
ec2 = session.client('ec2')
response = ec2.describe_instances()
#format your row and write to the .csv
print(response)
