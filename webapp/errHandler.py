from rest_framework import status
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.response import Response
import logging
logger = logging.getLogger('app_api') #from LOGGING.loggers in settings.py


class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        if isinstance(exception, ValidationError):
            return Response({"success": False, "reason": ValidationError.__cause__}, status=status.HTTP_400_BAD_REQUEST)
        
        if isinstance(exception, IntegrityError):

            return Response({"success": False, "reason": IntegrityError.__cause__}, status=status.HTTP_409_CONFLICT)
        else:
            logger.info(3, exception)

        return None 