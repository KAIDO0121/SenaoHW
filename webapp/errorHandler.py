from rest_framework.views import exception_handler
from .exceptions import ValidationErr
from rest_framework.response import Response
from rest_framework.exceptions import ErrorDetail


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None and isinstance(exc.detail, ErrorDetail):
        
        return Response({"success": False, "reason": exc.detail}, status=response.status_code)
    
    return response