from django.urls import include, path
from .views import UserCreate, UserVerify


urlpatterns = [
    path('user/', UserCreate.as_view(), name='create-user'),
    path('session/', UserVerify.as_view(), name='verify-customer')
]