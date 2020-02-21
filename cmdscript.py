import requests
import sys

url = sys.argv[1]
r = requests.get(URL_of_AWS_Lambda_API_Gateway+'url?url='+url)
