import json
import requests
from django_fcm_http_v1.default_settings import DEFAULT_SETTINGS
from django_fcm_http_v1.errors_handlers import FCMError, FCMInvalidData, ImproperlyConfiguredError


class FCMManager:
    """
    FCMManager to send push notification to platforms:
    - android
    - ios
    - web
    - currently only `android` is supported
    """

    def __init__(self):
        self.service_file_path = DEFAULT_SETTINGS['FCM_SERVICE_FILE_PATH']
        if not self.service_file_path:
            raise ImproperlyConfiguredError("Please provide a service file")
        with open(self.service_file_path) as f:
            project_id = json.loads(f.read()).get('project_id', None)
            if not project_id:
                raise RuntimeError("Project ID is empty")
        self.base_url = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"

    def get_access_token(self):
        from oauth2client.service_account import ServiceAccountCredentials

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.service_file_path, scopes=['https://www.googleapis.com/auth/firebase.messaging'])

        return credentials.get_access_token().access_token

    @staticmethod
    def tokens_to_list(tokens):
        if not isinstance(tokens, list):
            tokens = [tokens]
        return tokens

    @staticmethod
    def validate_input(data: dict, tokens: list, notification: dict):
        if not isinstance(data, dict):
            raise FCMInvalidData("Data is not a dictionary")
        if not isinstance(tokens, list):
            raise FCMInvalidData("Tokens is not a list")
        if not isinstance(notification, dict):
            print(notification)
            # raise FCMInvalidData("Notification is not a dictionary")
            pass

    """
    Send push notification to specified tokens
    - data: dict
    - notification: FCMNotification
    - android: FCMAndroid
    - tokens: list
    """
    def send_message(self, data: dict, tokens: list, notification: dict, direct_boot_ok=True, **kwargs):
        tokens = self.tokens_to_list(tokens)
        self.validate_input(data=data, tokens=tokens, notification=notification)

        for token in tokens:
            payload = {
                "message": {
                    "token": token,
                    "notification": notification,
                    "data": data,
                    "android": kwargs.get('android', {
                        "direct_boot_ok": direct_boot_ok
                    }),
                    **kwargs
                }
            }

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {self.get_access_token()}",
            }

            response = requests.post(
                self.base_url, json=payload, headers=headers)
            if response.status_code != 200:
                print(response.text)
                raise FCMError('FCM error: ' + response.text)
            return response.json()
