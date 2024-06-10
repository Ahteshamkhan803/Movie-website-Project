

from django.contrib import admin
from Movie_App.models import Movies_model, Review_Model,Platforms_model

# Register your models here.

class Movie_Admin(admin.ModelAdmin):
    list_display=['id','Movie_Name','Movie_Rating','Movie_ReleaseYear','Movie_Language','Movie_Subtitle','Movie_Size','Movie_Quality','Movie_Format','Movie_Story','is_Movie_Webseries','is_Movie_DualAudio','Movie_Created','Movie_Platform','Movie_Upload','Movies_ScreenShots']
admin.site.register(Movies_model,Movie_Admin)




class review_Admin(admin.ModelAdmin):
    list_display= ['id','user','Review_Text','Created_At','Review_Movie_name']
admin.site.register(Review_Model,review_Admin)



class platform_Admin(admin.ModelAdmin):
    list_display=['id','Name_Platform','About_Platform','Website_Platform']
admin.site.register(Platforms_model,platform_Admin)

