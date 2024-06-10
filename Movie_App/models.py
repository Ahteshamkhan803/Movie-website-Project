from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
# Create your models here.


# this model is for platform like netflix amazon prime etc
class Platforms_model(models.Model):
    Name_Platform=models.CharField(max_length=50)
    About_Platform=models.CharField(max_length=50)
    Website_Platform=models.URLField(max_length=100)

    def __str__(self) :
        return self.Name_Platform
    


  
# class Review_Model(models.Model):
#     # Review_Movie_name=models.ForeignKey(Movies_model,on_delete=models.CASCADE,related_name='Review')
#     # created_by_name= models.ForeignKey(User ,on_delete=models.CASCADE, related_name='created_by_name')
#     user= models.ForeignKey(User, on_delete=models.CASCADE)

#     Created_At= models.DateTimeField(auto_now_add=True)
#     Review_Text= models.CharField(max_length=200)

#     # class Meta:
#     #     unique_together= ('Review_Movie_name','user')

#     def __str__(self):
#         return f"Review by {self.user.username}"
    

# this model is for uploading movies

class Movies_model(models.Model):

    Language_Choices=[
        ('Hindi','Hindi'),
        ('English','English'),
        ('Marathi','Marathi'),
        ('Tamil','Tamil'),


    ]

    Movie_Subtitles=[
        ('Hindi','Hindi'),
        ('English','English')
    ]

    Movie_Quality=[
        ('480P','480P'),
        ('720P','720P'),
        ('1080p','1080p')

    ]

    Movie_Format=[
        ('MKV','MKV')
    ]

    Movie_Name=models.CharField(max_length=100)
    Movie_Rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    Movie_ReleaseYear=models.DateField()
    Movie_Language=models.CharField(max_length=7,choices=Language_Choices)
    Movie_Subtitle=models.CharField(max_length=7,choices=Movie_Subtitles)
    Movie_Size=models.PositiveIntegerField()
    Movie_Quality=models.CharField(max_length=5,choices=Movie_Quality)
    Movie_Format=models.CharField(max_length=3,choices=Movie_Format)
    Movie_Story=models.CharField(max_length=1000)
    is_Movie_Webseries=models.BooleanField(default=False)
    is_Movie_DualAudio=models.BooleanField(default=False)
    Movie_Created=models.DateTimeField(auto_now_add=True)
    Movie_Platform=models.ForeignKey(Platforms_model,on_delete=models.CASCADE,related_name='Movies')
    Movie_Upload= models.FileField(upload_to='Movies/')
    Movies_ScreenShots=models.ImageField(upload_to='Movie_ScreenShot/')
    # Movies_Review=models.ForeignKey(Review_Model,on_delete=models.CASCADE,related_name='Movies_Review')
    

    def __str__(self):
        return self.Movie_Name
    






class Review_Model(models.Model):
    Review_Movie_name = models.ForeignKey(Movies_model, on_delete=models.CASCADE, related_name='Reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_At = models.DateTimeField(auto_now_add=True)
    Review_Text = models.CharField(max_length=200)

    class Meta:
        unique_together = ('Review_Movie_name', 'user')

    def __str__(self):
        return f"Review for {self.Review_Movie_name.Movie_Name} by {self.user.username}"    



# custom auth model

