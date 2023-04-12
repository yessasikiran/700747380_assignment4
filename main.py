import boto3

# Create an SNS client
sns = boto3.client('sns')

# Create a new SNS topic
response = sns.create_topic(
    Name='My-12345845858'
)

# Get the ARN of the new topic
topic_arn = response['TopicArn']

# Add an email address as a subscriber to the topic
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='yespvin@gmail.com'
)

# Print the subscription ARN
print('Subscription ARN:', response['SubscriptionArn'])