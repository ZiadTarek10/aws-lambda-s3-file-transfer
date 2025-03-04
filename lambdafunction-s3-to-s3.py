import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Extract information from the S3 event
    source_bucket = 'sourcebucket-zizo'  # Source bucket name
    object_key = event['Records'][0]['s3']['object']['key']  # The uploaded object key
    
    # Specify the target bucket
    target_bucket = 'targetbucket-ziadtarek'  # Target bucket name

    # Copy the file from source bucket to target bucket
    copy_source = {'Bucket': source_bucket, 'Key': object_key}
    s3.copy_object(CopySource=copy_source, Bucket=target_bucket, Key=object_key)
    
    return {
        'statusCode': 200,
        'body': f"File {object_key} copied from {source_bucket} to {target_bucket}"
    }
