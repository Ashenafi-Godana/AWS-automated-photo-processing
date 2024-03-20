import json
import boto3

def lambda_handler(event, context):
    # Get the bucket and object key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Process the uploaded file (Here, we just print the details)
    print(f"File uploaded: s3://{bucket}/{key}")
    
    # Publish a message to SNS topic
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:576604583562:photo-processor',
        Message=json.dumps({'default': json.dumps({'bucket': bucket, 'key': key})}),
        MessageStructure='json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }
