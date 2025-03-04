import requests
import boto3

def lambda_handler(event, context):
    url = "https://raw.githubusercontent.com/username/repository/main/config.json"
    
    response = requests.get(url)
    if response.status_code == 200:
        s3 = boto3.client("s3")
        s3.put_object(Bucket="your-bucket-name", Key="config.json", Body=response.content)
        return "File copied to S3 successfully"
    else:
        return f"Failed to fetch file: {response.status_code}"
