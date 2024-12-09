import boto3 # type: ignore


def lambda_handler(event, context):

    client = boto3.client('rds')
    
    rdslist = ['pnb-uat-gst-sahay-db', 'preprod-bob-db']
    for i in rdslist:
        response = client.describe_db_instances(DBInstanceIdentifier=i)
        status = response['DBInstances'][0]['DBInstanceStatus']
    
        if status == 'stopped':
            client.start_db_instance(DBInstanceIdentifier=i)
            print ("starting")
        else:
            print(status)