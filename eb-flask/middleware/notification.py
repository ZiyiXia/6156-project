import requests
import json
import middleware.context as context
import boto3


class NotificationMiddlewareHandler:
    sns_client = None

    sns_arn = 'arn:aws:sns:us-east-2:719950645153:6156-TBD'

    paths = {'path': ['/', '/api'], 'method': ['GET', 'POST', 'DELETE', 'PUSH']}

    def __init__(self):
        pass

    @classmethod
    def get_client(cls):
        ACCESS_ID = 'AKIA2PIDHA6QULZ2MRNR'
        ACCESS_KEY = 'ZHRr8Q0aJMsGbf4Qhsx+flWKcD0WPL5wl6yrEqc+'
        if NotificationMiddlewareHandler.sns_client is None:
            NotificationMiddlewareHandler.sns_client = boto3.client('sns', region_name='us-east-2')
            # NotificationMiddlewareHandler.sns_client = boto3.resource('sns', region_name='us-east-2')

        return NotificationMiddlewareHandler.sns_client

    @classmethod
    def send_message(cls, sns_topic, message):
        client = NotificationMiddlewareHandler.get_client()
        resp = client.publish(
            TopicArn=sns_topic,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        print("response = ", json.dumps(resp, indent=2))

    @staticmethod
    def notify(request, response):
        message = {'path': request.path, 'method': request.method}
        NotificationMiddlewareHandler.send_message(NotificationMiddlewareHandler.sns_arn, message)
        response = message
        print("done")
        return response
