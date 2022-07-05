from django.db import models
from django_fcm_http_v1.fcmManager import FCMManager

PLATFORMS = (
    ('android', 'android'),
    ('ios', 'ios'),
    ('web', 'web'),
)


class DeviceManager(models.Manager):
    def create_device(self, token, name, platform, **extra_fields):
        for p in PLATFORMS:
            if platform in p[0]:
                break
            else:
                raise ValueError(f"Platform {platform} is not supported")
        device = self.create(token=token, name=name,
                             platform=platform, **extra_fields)
        return device


class DeviceAbstract(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    platform = models.CharField(max_length=10, choices=PLATFORMS)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DeviceManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.token

    def send_message(self, data: dict, notification: dict, tokens: list, direct_boot_ok=True):
        try:
            FCMManager().send_message(
                data=data, notification=notification, tokens=tokens, direct_boot_ok=direct_boot_ok)
        except Exception as e:
            raise e


class Device(DeviceAbstract):
    pass
