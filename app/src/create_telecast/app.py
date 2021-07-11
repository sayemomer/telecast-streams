import json
import boto3
import os

# import requests

dynamo = boto3.client('dynamodb')
table_name = os.environ['TABLE_NAME']
region = os.environ['REGION_NAME']


def lambda_handler(message, context):

    activity = json.loads(message['body'])

    print(activity)

    params = {
        'id': {
            "S": "12121"
        },
        'start_time': activity['start_time'],
        'end_time': activity['end_time']
    }

    response =  dynamo.put_item(
        TableName=table_name,
        Item=params
    )

    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Activity created'})
    }
