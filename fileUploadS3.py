import json
import boto3
from botocore.vendored import requests

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client("s3")
    if event:
        print("Event: ", event)
        file_obj = event["Records"][0]
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket = BUCKET_NAME, Key=filename)
        if filename.endswith('hash.json'):
            print('cool')
        else:
            URL = "http://"+IP_Address_of_EC2_instance
            PARAMS = {'filename':filename}
            r = requests.get(url = URL, params = PARAMS)
        
    print("Hi")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
