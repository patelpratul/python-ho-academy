import boto3
import schedule

# Before refactor
# ec2_client = boto3.client('ec2', region_name="eu-west-2")

# volumes = ec2_client.describe_volumes()["Volumes"]

# for volume in volumes:
#     new_snapshot=ec2_client.create_snapshot(
#         VolumeId=volume["VolumeId"]
#     )
#     print(new_snapshot)


ec2_client = boto3.client('ec2', region_name="eu-west-2")

def create_volume_snapshots():

    volumes = ec2_client.describe_volumes()["Volumes"]

    for volume in volumes:
        new_snapshot=ec2_client.create_snapshot(
            VolumeId=volume["VolumeId"]
        )
        print(new_snapshot)

schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()

# filter by Volume ID

# def create_volume_snapshots():

#     volumes = ec2_client.describe_volumes(
#         Filters=[
#             {
#                 'Name': 'tag:Environment',
#                 'Values': ['prod', 'dev']
#             }
#         ]
#     )

#     for volume in volumes['Volumes']:
#         new_snapshot = ec2_client.create_snapshot(
#             VolumeId=volume['VolumeId']
#         )
#         print(new_snapshot)
