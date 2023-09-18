"""Defines the url patterns for the users"""
from django.urls import path, include 
from . import views # importing view to enable user registration

app_name = 'users'

urlpatterns = [
    # Include the default authentication urls
    path('', include('django.contrib.auth.urls')),
    # Registration Page
    path('register/',views.register,name='register'),
]
