from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password




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
