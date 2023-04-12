import boto3

# Create an SNS client
sns = boto3.client('sns')

# Subscribe an email address to an SNS topic
response = sns.subscribe(
    TopicArn='arn:aws:sns:REGION:ACCOUNT_ID:TOPIC_NAME',
    Protocol='email',
    Endpoint='you@example.com'
)

# Print the subscription ARN
print('Subscription ARN:', response['SubscriptionArn'])
