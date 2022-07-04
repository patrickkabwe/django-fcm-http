from django.test import TestCase
from django_fcm_http_v1.errors_handlers import FCMError
from django_fcm_http_v1.fcmManager import FCMManager

from django_fcm_http_v1.models import Device

# Create your tests here.

fcm_token = "fcm_token"


class TestFCMManager(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_should_return_token(self):
        token = FCMManager().get_access_token()
        self.assertIsNotNone(token)


class TestDeviceModel(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_device(self):
        device = Device.objects.create_device(
            token=fcm_token, name='name', platform='android', is_active=True)
        self.assertEqual(device.token, fcm_token)
        self.assertEqual(device.name, 'name')
        self.assertEqual(device.platform, 'android')
        self.assertEqual(device.is_active, True)

    def test_device_send_message(self):
        device = Device.objects.create_device(
            token=fcm_token, name='name', platform='android', is_active=True)
        device.send_message(data={}, notification={
                            'title': 'title', 'body': 'body'}, tokens=fcm_token)
        self.assertEqual(device.token, fcm_token)
