class FCMError(Exception):
    pass


class FCMInvalidToken(FCMError):
    pass


class FCMInvalidData(FCMError):
    pass


class ImproperlyConfiguredError(Exception):
    pass