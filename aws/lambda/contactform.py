import boto3
import os
import json


def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Credentials" : 'true'
            },
        }

def sendEmail(event, sender, receiver):
    ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                receiver
            ],
        },
        Message={
            'Subject': {
                'Data': 'name: ' + event.name + '\nemail: ' + event.email + '\ndesc: ' + event.messg
                'Charset': 'UTF-8'
            }
            'Subject': {
                'Data': 'You got mail! From: ' + event.name,
                'Charset': 'UTF-8'
            }
        }
    )

def handler(event, context):
    sender = os.environ['sender']
    receiver = os.environ['receiver']
    ses = boto3.client('ses')
    print('Received event:' + event)
    try:
        sendEmail(event, sender, receiver)
        return response({'message': 'all good'}, 200)
    except Exception as e:
        return response({'message': e.message}, 400)
