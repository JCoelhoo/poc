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
    raise Exception('Error')
    
    now = datetime.datetime.now()
    id = uuid.uuid4()
    item = {
        'id': str(id),
        'creationTime': str(now.timestamp())
    }

    try: 
        table.put_item(
            Item = item
        )
        return {
            "statusCode": 200,
            "body": json.dumps(str(id)),
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({
                'message': 'An error occured'
            }),
        }
