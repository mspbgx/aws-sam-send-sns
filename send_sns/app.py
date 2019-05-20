import boto3
import os

def lamda_sendMessage(event, context):
    topic_arn = os.environ.get('SNS_TOPIC_ARN')
    # Create an SNS client
    sns = boto3.client('sns')

    # Publish a simple message to the specified SNS topic
    response = sns.publish(
        TopicArn=topic_arn,    
        Message='My content',    
    )

    # Print out the response
    print(response)
			
    return {'code': 0, 'message': 'success'}