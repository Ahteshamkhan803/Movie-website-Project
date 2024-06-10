from rest_framework import serializers
from Movie_App.models import Platforms_model, Movies_model,Review_Model
from django.contrib.auth.models import User



# class Review_serializer(serializers.ModelSerializer):
#     Name_of_movie=serializers.CharField(source='Review_Movie_name',read_only=True)
#     # Name_of_movie=serializers.PrimaryKeyRelatedField(queryset=Movies_model.objects.all())
#     username = serializers.ReadOnlyField(source='user.username')
#     # Name_of_movie = serializers.ReadOnlyField(source='Review_Movie_name')
#     class Meta:
#         model= Review_Model
#         fields= ['id','Created_At','user','Review_Text','username','Name_of_movie']

#         #   fields= ['id','Movie_Name','Created_At','user','Review_Text','username']



# class Platform_serializer(serializers.ModelSerializer):
#     class Meta:
#         model= Platforms_model
#         fields= '__all__'       




# class Movie_serializer(serializers.ModelSerializer):
#     Review= Review_serializer(source='Name_of_movie',many=True)
#     platform_name= serializers.CharField(source='Movie_Platform',read_only=True)
#     class Meta:
#         model= Movies_model
#         fields= '__all__' 








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
    # Movie_name= Review_serializer(read_only=True,many=True)
    # Review= Review_serializer(read_only=True,many=True)
#     class Meta:
#         model= Movies_model
#         fields= '__all__'        

#     # Reviews= Review_serializer(source='Movies_Review',many=True)
#     # class Meta:
#     #     model= Movies_model
#     #     fields= '__all__'        



class Platforms_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Platforms_model
        fields = ['id', 'Name_Platform', 'About_Platform', 'Website_Platform']





class Review_Serializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    Movie_Name = serializers.SerializerMethodField()
    platform_name = serializers.SerializerMethodField()

    class Meta:
        model = Review_Model
        fields = ['id', 'Review_Movie_name', 'user', 'user_name','Movie_Name','platform_name','Created_At', 'Review_Text']
        read_only_fields = ['Created_At']

    
    def get_user_name(self, obj):
        return obj.user.username

    def get_Movie_Name(self, obj):
        return obj.Review_Movie_name.Movie_Name

    def get_platform_name(self, obj):
        return obj.Review_Movie_name.Movie_Platform.Name_Platform    

    def validate(self, data):
       
        if Review_Model.objects.filter(Review_Movie_name=data['Review_Movie_name'], user=data['user']).exists():
            raise serializers.ValidationError("You have already reviewed this movie.")
        return data




class Movies_Serializer(serializers.ModelSerializer):
     Reviews= Review_Serializer(read_only=True,many=True)
     class Meta:
         model = Movies_model
         fields = [
            'id', 'Movie_Name', 'Movie_Rating', 'Movie_ReleaseYear', 'Movie_Language',
            'Movie_Subtitle', 'Movie_Size', 'Movie_Quality', 'Movie_Format', 'Movie_Story',
            'is_Movie_Webseries', 'is_Movie_DualAudio', 'Movie_Created', 'Movie_Platform',
            'Movie_Upload', 'Movies_ScreenShots','Reviews'
        ]

 
  
   




