from rest_framework.exceptions import APIException
from rest_framework import status

class Throttled(APIException):
    default_detail = "Custom Exception Message"
    default_success = False

    def __init__(self, detail, code = None):
        self.detail = detail
        self.status_code = status.HTTP_429_TOO_MANY_REQUESTS

class AuthenticateErr(APIException):
    default_detail = "Custom Exception Message"
    default_success = False

    def __init__(self, detail, code = None):
        self.detail = detail
        self.status_code = status.HTTP_401_UNAUTHORIZED

class EntityNotFoundErr(APIException):
    default_detail = "Custom Exception Message"
    default_default_success = False


    def __init__(self, detail, code = None):
        self.detail = detail
        self.status_code = status.HTTP_404_NOT_FOUND

class ValidationErr(APIException):
    default_detail = "Custom Exception Message"
    default_success = False
    status_code = status.HTTP_400_BAD_REQUEST


    def __init__(self, detail, code = None):
        self.detail = detail
        self.status_code = code

class IntegrityErr(APIException):
    default_detail = "Custom Exception Message"
    default_success = False

    def __init__(self, detail, code = None):
        self.detail = detail
        self.status_code = status.HTTP_409_CONFLICT