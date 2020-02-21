from flask import Flask, render_template, request
import boto3
import hashlib
import json

app = Flask(__name__)

@app.route("/")
def home_func():
    filename = request.args['filename']
    print(filename)
    hashfilename = filename.replace('.json', '')
    hashfilename = hashfilename + 'hash.json'
    sha256_hash = hashlib.sha256()
    s3 = boto3.client("s3", aws_access_key_id = Enter_Access_key, aws_secret_access_key = Enter_Access_Password)
    fileObj = s3.get_object(Bucket = Bucket_Name, Key = filename)
    file_content = fileObj["Body"].read()
    sha256_hash.update(file_content)
    hashvalue = sha256_hash.hexdigest()
    with open("/tmp/log.json", "w") as f:
            json.dump(hashvalue, f)
    s3.upload_file("/tmp/log.json", Bucket_Name, hashfilename)
    return render_template("home.html")
