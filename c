import requests
import sys

url = sys.argv[1]
r = requests.get('https://jc10fl3o4k.execute-api.us-east-2.amazonaws.com/urldownload/url?url='+url)
