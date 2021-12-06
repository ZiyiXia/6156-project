import requests
import json
import middleware.context as context

class NotificationMiddlewareHandler:
    sns_url = ''
    def __init__(self):
        pass
    @staticmethod
    def notify(request, response):

        subscriptions = context.get_context("SUBSCRIPTIONS")

        if request.path in subscriptions:

            notification = {}

            try:
                request_data = request.get_json()
            except Exception as e:
                request_data = None

            path = request.path

            if request.method == 'POST':
                notification["change"] = "CREATED"
                notification['new_state'] = request_data
                notification['params'] = path
            elif request.method == 'PUT':
                notification['change'] = 'UPDATE'
                notification['new_state'] = request_data
                notification['params'] = path
            elif request.method == 'DELETE':
                notification['change'] = 'DELETED'
                notification['params'] = path
            else:
                notification = None

            if notification.get("change", None):
                request_data = json.dumps(notification)
                request_data = json.dumps({'text': request_data}).encode('utf-8')
                response =request.post(
                    NotificationMiddlewareHandler.sns_url,data=request_data,
                    headers={'Content-Type': 'application/json'}
                )
                print("Response = ", response.status_code)


