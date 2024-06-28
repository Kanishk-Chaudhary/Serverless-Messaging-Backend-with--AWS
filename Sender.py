import boto3
import json

# Initialize SQS client
sqs = boto3.client('sqs')

# Replace 'queue_url' with your actual queue URL
queue_url = 'https://sqs.ap-south-1.amazonaws.com/417117090286/ChatAPP'

# Sample JSON data
data = {
    'user_id': 123,
    'message': 'Hello from Kanishk',
    'timestamp': '2024-06-28T12:00:00Z'
}

# Convert Python dictionary to JSON string
message_body = json.dumps(data)

# Send a message to the queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=message_body
)

# Print the response (includes message ID and MD5 of the body)
print(f"MessageId: {response['MessageId']}")
