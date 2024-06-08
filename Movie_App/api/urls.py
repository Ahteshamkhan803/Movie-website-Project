from django.contrib import admin
from django.urls import path,include
from Movie_App.api.views import Platform_view, Review_Details_view, Review_View, movies_view,Movies_Details_view 
from rest_framework.routers import DefaultRouter




router=DefaultRouter()
router.register(r'Reviews',Review_View)







urlpatterns=[
    path('Movies/',movies_view.as_view(),name='movies-list'),
    path('Movies/<int:pk>/',Movies_Details_view.as_view(),name='movie-detail'),
    path('platform/',Platform_view.as_view(),name='platform-list'),
    path('', include(router.urls))

]