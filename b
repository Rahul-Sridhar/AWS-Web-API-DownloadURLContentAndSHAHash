import json
import urllib.request
import boto3

def lambda_handler(event, context):
    url = event['url']
    
    fp = urllib.request.urlopen(url)
    encode_response = fp.read()
    response = encode_response.decode("utf8")
    fp.close()
    
    s3 = boto3.client("s3")
    with open("/tmp/log.json", "w") as f:
        json.dump(response, f)
    url = url.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    #url = url.replace('/', '_')
    s3.upload_file("/tmp/log.json", "mjrf2320", url+".json")
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(url)
    }
