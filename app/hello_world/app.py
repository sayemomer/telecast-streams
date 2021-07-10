import json
import boto3
import os

# import requests

dynamo = boto3.client('dynamodb')
table_name = os.environ['TABLE_NAME']
region = os.environ['REGION_NAME']


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    scan_result = dynamo.scan(TableName=table_name)
    print(scan_result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "query_result": scan_result
            # "location": ip.text.replace("\n", "")
        }),
    }
