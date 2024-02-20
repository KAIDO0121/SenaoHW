from rest_framework import status
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import exception_handler
import logging
logger = logging.getLogger('app_api') #from LOGGING.loggers in settings.py


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        print('========================', response)
        # if isinstance(exception, ValidationError):
        #     return Response({"success": False, "reason": ValidationError.__cause__}, status=status.HTTP_400_BAD_REQUEST)
        
        # if isinstance(exception, IntegrityError):

        #     return Response({"success": False, "reason": IntegrityError.__cause__}, status=status.HTTP_409_CONFLICT)
        # else:
        #     logger.info(3, exception)

        return None 