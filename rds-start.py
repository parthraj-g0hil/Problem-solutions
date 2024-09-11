import boto3 # type: ignore


def lambda_handler(event, context):

    client = boto3.client('rds')
    
    rdslist = ['pnb-uat-gst-sahay-db', 'preprod-bob-db', 'qa-fitscore-db', 'qa-gst-sahay-db', 'qa-opl-db', 'sit-gst-sahay-db', 'sit-oam-db','uat-fitscore-db', 'uat-gst-sahay-db', 'uat-hsbc-db','qa-oam-db','uat-oam-db', 'uat-opl-db','qa-hsbc-db']
    for i in rdslist:
        response = client.describe_db_instances(DBInstanceIdentifier=i)
        status = response['DBInstances'][0]['DBInstanceStatus']
    
        if status == 'stopped':
            client.start_db_instance(DBInstanceIdentifier=i)
            print ("starting")
        else:
            print(status)