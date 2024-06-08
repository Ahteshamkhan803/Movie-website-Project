from rest_framework import serializers
from Movie_App.models import Platforms_model, Movies_model,Review_Model



class Review_serializer(serializers.ModelSerializer):
    Movie=serializers.CharField(source='Review_Movie_name.Movie_Name',read_only=True)
    username= serializers.ReadOnlyField(source='user.username')
    class Meta:
        model= Review_Model
        fields= ['id','Created_At','user','Review_Text','username','Movie']

        #   fields= ['id','Movie_Name','Created_At','user','Review_Text','username']



class Platform_serializer(serializers.ModelSerializer):
    class Meta:
        model= Platforms_model
        fields= '__all__'       




class Movie_serializer(serializers.ModelSerializer):
    Review= Review_serializer(source='Name_of_movie',many=True)
    platform_name= serializers.CharField(source='Movie_Platform.Name_Platform',read_only=True)
    class Meta:
        model= Movies_model
        fields= '__all__' 








# class Review_serializer(serializers.ModelSerializer):
#     # Movie_Name=serializers.CharField(source='Review_Movie_name.Movie_Name',read_only=True)
#     username= serializers.ReadOnlyField(source='user.username')
#     class Meta:
#         model= Review_Model
#         fields= ['id','Created_At','user','Review_Text','username']

#         #   fields= ['id','Movie_Name','Created_At','user','Review_Text','username']



# class Platform_serializer(serializers.ModelSerializer):
#     class Meta:
#         model= Platforms_model
#         fields= '__all__'       



# class Movie_serializer(serializers.ModelSerializer):
#     Movies_Review= Review_serializer(source='Movies_Review',many=True)
#     class Meta:
#         model= Movies_model
#         fields= '__all__'        

# from rest_framework import serializers
# from Movie_App.models import Platforms_model, Movies_model,Review_Model









# class Review_serializer(serializers.ModelSerializer):
#     # Movie_Name=serializers.CharField(source='Review_Movie_name.Movie_Name',read_only=True)
#     Movie_Name = serializers.ReadOnlyField(source='Review_Movie_name.Movie_Name')
#     username= serializers.ReadOnlyField(source='user.username')
#     class Meta:
#         model= Review_Model
#         fields= ['id','Created_At','user','Review_Text','username','Movie_Name']

#         #   fields= ['id','Movie_Name','Created_At','user','Review_Text','username']



# class Platform_serializer(serializers.ModelSerializer):
#     class Meta:
#         model= Platforms_model
#         fields= '__all__'       



# class Movie_serializer(serializers.ModelSerializer):
#     Movie_name= Review_serializer(read_only=True,many=True)
#     # Review= Review_serializer(read_only=True,many=True)
#     class Meta:
#         model= Movies_model
#         fields= '__all__'        

#     # Reviews= Review_serializer(source='Movies_Review',many=True)
#     # class Meta:
#     #     model= Movies_model
#     #     fields= '__all__'        

