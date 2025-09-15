import boto3

# Get each instances ids
# store ids
# append tags based on ids

# ec2_client_london = boto3.client('ec2', region_name="eu-west-2")
# ec2_client_ireland = boto3.client('ec2', region_name="eu-west-1")

# instance_ids_london=[]
# instance_ids_ireland=[]


# reservations_london = ec2_client_london.describe_instances()['Reservations']
# reservations_ireland = ec2_client_ireland.describe_instances()["Reservations"]

# #London
# for res in reservations_london:
#     instances = res['Instances']
#     for ins in instances:
#         ids = ins["InstanceId"]
#         instance_ids_london.append(ids)


# response = ec2_client_london.create_tags(
#     Resources=instance_ids_london,
#     Tags=[
#         {
#             'Key': 'Environment',
#             'Value': 'Prod'
#         },
#     ]
# )

# #Ireland

# for res in reservations_ireland:
#     instances = res['Instances']
#     for ins in instances:
#         ids = ins["InstanceId"]
#         instance_ids_ireland.append(ids)


# response = ec2_client_ireland.create_tags(
#     Resources=instance_ids_ireland,
#     Tags=[
#         {
#             'Key': 'Environment',
#             'Value': 'Development'
#         },
#     ]
# )


# Refactored

def tag_instances(region, tag_value):
    ec2_client = boto3.client('ec2', region_name=region)

    instance_ids = []
    reservations = ec2_client.describe_instances()["Reservations"]

    for res in reservations:
        for ins in res["Instances"]:
            instance_ids.append(ins["InstanceId"])

        if instance_ids: # Only tag if instances exist
            ec2_client.create_tags(
                Resources=instance_ids,
                Tags=[
                    {
                        'Key': 'Environment',
                        'Value': tag_value
                    },
                ]
            )
            print(f"Tagged {len(instance_ids)} instances in {region} as {tag_value}")
        else:
            print(f"No instances found in {region}")



tag_instances("eu-west-2", "Prod")
tag_instances("eu-west-1", "Development")