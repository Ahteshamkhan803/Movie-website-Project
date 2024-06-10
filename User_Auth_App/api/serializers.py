from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class Registr_Serializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True, required=True, validators=[validate_password])
    Con_password= serializers.CharField(write_only=True, required=True,validators=[validate_password])




    class Meta:
        model= User
        fields = ('username', 'password', 'Con_password', 'email', 'first_name', 'last_name')



    def validate(self,attrs):
        if attrs['password'] != attrs['Con_password']:
            raise serializers.ValidationError({"password": "password is not match"})
        return attrs
    

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Emial is already register")
        return value

    
    

    




    def create(self, validated_data):
        user= User.objects.create(
            username= validated_data['username'],
            email= validated_data['email'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user





#login functionality


# In User_Auth_App/api/serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.')

            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')

            refresh = RefreshToken.for_user(user)

            return {
                'username': user.username,
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }
        else:
            raise serializers.ValidationError('Must include "username" and "password".')
