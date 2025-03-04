import json
import boto3
import os

# Initialize AWS clients
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

# Define DynamoDB table name
TABLE_NAME = "S3-file-names"

def lambda_handler(event, context):
    try:
        # Extract file name from the event
        records = event.get("Records", [])
        if not records:
            return {"statusCode": 400, "body": "No records found in the event"}

        for record in records:
            s3_bucket = record["s3"]["bucket"]["name"]
            file_name = record["s3"]["object"]["key"]
            
            # Get reference to the DynamoDB table
            table = dynamodb.Table(TABLE_NAME)

            # Insert file name into DynamoDB
            table.put_item(
                Item={
                    "FileName": file_name,
                    "S3Bucket": s3_bucket
                }
            )

        return {"statusCode": 200, "body": "File name stored in DynamoDB successfully"}

    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
