from rest_framework.exceptions import ParseError
from rest_framework import status

class Throttled(ParseError):
    default_detail = "Custom Exception Message"
    default_success = False


    def __init__(self, detail):
        self.detail = detail
        self.statusCode = status.HTTP_429_TOO_MANY_REQUESTS

class AuthenticateErr(ParseError):
    default_detail = "Custom Exception Message"
    default_success = False


    def __init__(self, detail):
        self.detail = detail
        self.statusCode = status.HTTP_401_UNAUTHORIZED

class EntityNotFoundErr(ParseError):
    
    default_detail = "Custom Exception Message"
    default_success = False


    def __init__(self, detail):
        self.detail = detail
        self.statusCode = status.HTTP_404_NOT_FOUND

class ValidationErr(ParseError):
    statusCode = status.HTTP_400_BAD_REQUEST
    default_detail = "Custom Exception Message"
    default_success = False


    def __init__(self, detail, statusCode):
        self.detail = detail
        self.statusCode = statusCode

class IntegrityErr(ParseError):
    statusCode = status.HTTP_409_CONFLICT
    default_detail = "Custom Exception Message"
    default_success = False


    def __init__(self, detail, statusCode):
        self.detail = detail
        self.statusCode = statusCode