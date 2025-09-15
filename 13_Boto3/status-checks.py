import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-west-2")

# Before refactor
# statuses = ec2_client.describe_instance_status()

# for status in statuses["InstanceStatuses"]:
#     ins_status = status["InstanceStatus"]["Status"]
#     sys_status = status['SystemStatus']['Status']
#     state = status["InstanceState"]["Name"]
#     instance_id = status["InstanceId"]
#     print(f"Instance {instance_id} is {state} with instance status {ins_status} and system status {sys_status}")
# print("#############################\n")

# After refactor + schedule

def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")
    print("#############################\n")


schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()
