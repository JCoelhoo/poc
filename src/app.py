import json
# aws python sdk
import boto3
import datetime
import uuid
import os

# dynamodb client
dynamodb = boto3.resource('dynamodb')
# environment variable is set from the template.yaml
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    now = datetime.datetime.now()
    id = str(uuid.uuid4())

    try: 
        table.put_item(
            Item={
                'id': id,
                'creationTime': str(now.timestamp())
            }
        )
        return {
            "statusCode": 200,
            "body": json.dumps({
                'id': id,
                'creationTime': str(now.timestamp())
            }),
        }
    except:
        return {
            "statusCode": 500,
            "body": json.dumps({
                'message': 'An error occured'
            }),
        }
