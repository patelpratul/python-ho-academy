import boto3
 
ec2_client = boto3.client("ec2", region_name= "eu-west-2")
 
ec2_describe = ec2_client.describe_instances()
 
print(ec2_describe)