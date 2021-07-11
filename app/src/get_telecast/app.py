import json
import boto3
import os

# import requests

dynamo = boto3.client('dynamodb')
table_name = os.environ['TABLE_NAME']

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


