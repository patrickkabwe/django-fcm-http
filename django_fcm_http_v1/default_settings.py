from pathlib import Path
from django.conf import settings

from django_fcm_http_v1.errors_handlers import ImproperlyConfiguredError


DEFAULT_SETTINGS = {
    'FCM_SERVICE_FILE_PATH': f"{Path(settings.BASE_DIR)}/fcm_service_account.json",
}

if not hasattr(settings, 'FCM_SERVICE_FILE_PATH'):
    raise ImproperlyConfiguredError(
        "Please provide a FCM_SERVICE_FILE_PATH setting")
else:
    if not Path(settings.FCM_SERVICE_FILE_PATH).exists():
        raise ImproperlyConfiguredError(
            "FCM_SERVICE_FILE_PATH does not exist"
        )
    DEFAULT_SETTINGS['FCM_SERVICE_FILE_PATH'] = settings.FCM_SERVICE_FILE_PATH
