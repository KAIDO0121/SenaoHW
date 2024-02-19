from rest_framework import serializers, status
from .exceptions import ValidationErr, IntegrityErr, EntityNotFoundErr, AuthenticateErr
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from rest_framework.response import Response
from .models import User
import logging
import re
logger = logging.getLogger('app_api') #from LOGGING.loggers in settings.py

# class BaseUserSerializer():
    
    
#     def to_internal_value(self, payload):
#         print('payload', payload)
#         self.validate_username(payload.get('username'))
#         self.validate_password(payload.get('password'))
#         return {
#             'username': payload['username'],
#             'password': payload['password'],

#         }

#     def validate_username(self, username):

#         if not username or len(username) < 3 or len(username) > 32:
#             raise ValidationErr(detail = {"reason": "UserName must have a minimum length of 8 characters and a maximum length of 32 characters", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)
            
#         return username

#     def validate_password(self, password):
#         if not password or len(password) < 3 or len(password) > 32:
#             raise ValidationErr(detail = {"reason": "Passwords must have a minimum length of 8 characters and a maximum length of 32 characters", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)
        
#         if not re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$', password):
#             raise ValidationErr(detail = {"reason": "Passwords must have at least 1 uppercase letter, 1 lowercase letter, and 1 number.", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)

#         return password

class UserVerifySerializer(serializers.ModelSerializer):
    def to_internal_value(self, payload):
        self.validate_username(payload.get('username'))
        self.validate_password(payload.get('password'))
        return {
            'username': payload['username'],
            'password': payload['password'],

        }

    def validate_username(self, username):

        if not username or len(username) < 3 or len(username) > 32:
            raise ValidationErr(detail = {"reason": "Invalid username", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)
            
        return username

    def validate_password(self, password):
        if not password or len(password) < 3 or len(password) > 32:
            raise ValidationErr(detail = {"reason": "Invalid password", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)
        
        if not re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$', password):
            raise ValidationErr(detail = {"reason": "Invalid password", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)

        return password
    
    class Meta:
        model = User 
        fields = ['username', 'password']
    
    def authenticate(self, attrs):
        user = User.objects.filter(username = attrs.get('username')).values()
        

        if not user:
            raise EntityNotFoundErr(detail = {"reason": "UserName does not exist", "success":False})
        user = list(user)[0]
        
        if not check_password(attrs.get('password'), user.get('password')):
            raise AuthenticateErr(detail = {"reason": "Authenticate failed", "success":False})
        
        return attrs


class UserCreateSerializer(serializers.ModelSerializer):
    def to_internal_value(self, payload):
        self.validate_username(payload.get('username'))
        self.validate_password(payload.get('password'))
        return {
            'username': payload['username'],
            'password': payload['password'],

        }

    def validate_username(self, username):

        if not username or len(username) < 3 or len(username) > 32:
            raise ValidationErr(detail = {"reason": "UserName must have a minimum length of 8 characters and a maximum length of 32 characters", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)
            
        return username

    def validate_password(self, password):
        if not password or len(password) < 3 or len(password) > 32:
            raise ValidationErr(detail = {"reason": "Passwords must have a minimum length of 8 characters and a maximum length of 32 characters", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)
        
        if not re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$', password):
            raise ValidationErr(detail = {"reason": "Passwords must have at least 1 uppercase letter, 1 lowercase letter, and 1 number.", "success":False}, statusCode=status.HTTP_400_BAD_REQUEST)

        return password
    
    class Meta:
        model = User 
        fields = '__all__'
    
    def create(self, validated_data):
        
        hashed_pwd = make_password(validated_data['password'])
        try:
            User.objects.create(password = hashed_pwd, username = validated_data['username'])
        
        except IntegrityError as e:
            raise IntegrityErr(detail = {"reason": f'{e.__cause__}', "success":False}, statusCode=status.HTTP_409_CONFLICT)

        return validated_data
    # Response({"success": True}, status=status.HTTP_201_CREATED)
            