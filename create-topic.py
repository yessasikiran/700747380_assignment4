import boto3

# Initialize the client
sns_client = boto3.client('sns', region_name='us-east-1')

# Create an SNS topic
topic_name = 'my-topic'
response = sns_client.create_topic(Name=topic_name)