import boto3
import json

# Initialize SQS client
sqs = boto3.client('sqs')

# Replace 'queue_url' with your actual queue URL
queue_url = 'https://sqs.ap-south-1.amazonaws.com/417117090286/ChatAPP'

while True:
    print("Retrieving messages")
    
    # Receive messages from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,  # Adjust as needed
        WaitTimeSeconds=20,
    )
    
    # Check if there are any messages in the response
    if "Messages" in response:
        for message in response["Messages"]:
            try:
                # Parse message body as JSON
                message_body = json.loads(message['Body'])
                print(f"Message body: {message_body}")
                
                # Process your JSON data here
                user_id = message_body['user_id']
                message_text = message_body['message']
                timestamp = message_body['timestamp']
                
                # Example: Print the parsed data
                print(f"User ID: {user_id}, Message: {message_text}, Timestamp: {timestamp}")
                
                # Delete the message from the queue
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print(f"Removed message: {message['MessageId']}")
                
            except json.JSONDecodeError as e:
                print(f"Error parsing message JSON: {e}")
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print(f"Removed invalid message: {message['MessageId']}")
    
    else:
        print("No messages received")

    # Optional: Add a delay before retrieving messages again
    import time
    time.sleep(5)
