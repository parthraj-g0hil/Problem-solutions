import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Replace with your instance IDs
INSTANCE_IDS = [
    "i-0c9a1e987588304b7",  # qa-bob
    "i-0b41a769ad8af1a59"   # jfrog
]
REGION = "ap-south-1"  # Replace with your AWS region

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name=REGION)
    
    try:
        # Stop the instances
        response = ec2_client.stop_instances(InstanceIds=INSTANCE_IDS)
        logger.info(f"Stop response: {response}")
        
        # Fetch the current state of instances
        instance_states = response.get('StoppingInstances', [])
        result = [
            {
                "InstanceId": instance['InstanceId'],
                "State": instance['CurrentState']['Name']
            }
            for instance in instance_states
        ]
        
        logger.info(f"Instance states: {result}")
        return {
            "statusCode": 200,
            "body": result
        }
    
    except Exception as e:
        logger.error(f"Error stopping instances: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Failed to stop instances: {str(e)}"
        }
