import boto3

ec2_client_london = boto3.client('ec2', region_name="eu-west-2")
ec2_resource_london = boto3.resource('ec2', region_name="eu-west-2")

ec2_client_ireland = boto3.client('ec2', region_name="eu-west-1")
ec2_resource_ireland = boto3.resource('ec2', region_name="eu-west-1")

instance_ids_london = []
instance_ids_ireland = []

reservations_london = ec2_client_london.describe_instances()['Reservations']
for res in reservations_london:
    instances = res['Instances']
    for ins in instances:
        instance_ids_london.append(ins['InstanceId'])


response = ec2_resource_london.create_tags(
    Resources=instance_ids_london,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

reservations_ireland = ec2_client_ireland.describe_instances()['Reservations']
for res in reservations_ireland:
    instances = res['Instances']
    for ins in instances:
        instance_ids_ireland.append(ins['InstanceId'])


response = ec2_resource_ireland.create_tags(
    Resources=instance_ids_ireland,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
