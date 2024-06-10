from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import Registr_Serializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import LoginSerializer


class Register_view(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= Registr_Serializer
    permission_classes= [AllowAny]



    def create(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers= self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)
    


    #login view

    # In User_Auth_App/api/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import LoginSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
