import json
import boto3
import os

# import requests

dynamo = boto3.client('dynamodb')
table_name = os.environ['TABLE_NAME']
region = os.environ['REGION_NAME']


def create(message, context):

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


def lambda_handler(event, context):

    scan_result = dynamo.scan(TableName=table_name)
    print(scan_result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "query_result": scan_result
        }),
    }


