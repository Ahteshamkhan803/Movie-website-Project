from django.urls import path, include
from User_Auth_App.api.views import Register_view

urlpatterns = [
   path('register/',Register_view.as_view(), name='register')
]