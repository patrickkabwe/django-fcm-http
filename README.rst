==================
DJANGO FCM HTTP v1
==================

Django fcm http is a Django app to send push notifications to android, ios devices and web applications.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. First, install with pip:

    python -m pip install django-fcm-http

2. Add "django_fcm_http_v1" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_fcm_http_v1',
    ]

3. Create a firebase project and download the service_file.json file.

    Notice: Make sure you add the file in the root of your project.

4. Add "FCM_SERVICE_FILE_PATH" to your settings.py like this::

    FCM_SERVICE_FILE_PATH = '/path/to/service/file.json'

5. Run ``python manage.py migrate`` to create the device models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/polls/ to participate in the poll.