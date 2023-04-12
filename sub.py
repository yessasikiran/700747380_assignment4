import boto3
import configparser

# Read the topic name and email address from the config file
config = configparser.ConfigParser()
config.read('config.ini')
topic_name = config.get('SNS', 'TopicName')
email_address = config.get('SNS', 'EmailAddress')

# Create an SNS client
sns = boto3.client('sns')

# Create a new SNS topic
response = sns.create_topic(
    Name=topic_name
)

# Get the ARN of the new topic
topic_arn = response['TopicArn']

# Add an email address as a subscriber to the topic
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email_address
)

# Print the subscription ARN
print('Subscription ARN:', response['SubscriptionArn'])
