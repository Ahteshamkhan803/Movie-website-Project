from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import Registr_Serializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User





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