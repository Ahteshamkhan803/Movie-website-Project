from django.forms import ValidationError
from Movie_App.models import Movies_model, Platforms_model,Review_Model
from Movie_App.api.serializers import Movie_serializer, Platform_serializer,Review_serializer
from rest_framework import generics,viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
# from Movie_App.api.permission import IsOwnerOrReadOnly,IsAdminorReadonly
# from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend 
# from .filters import MovieFilter
# from Movie_App.api.pagination import Custompagination
from django.http import FileResponse, Http404
from rest_framework.views import APIView
import logging




class Platform_view(generics.ListCreateAPIView):
    queryset= Platforms_model.objects.all()
    serializer_class= Platform_serializer





class movies_view(generics.ListCreateAPIView):
    queryset= Movies_model.objects.all()
    serializer_class= Movie_serializer
    permission_classes=[IsAuthenticated]   #,IsAdminorReadonly
    filter_backends=[DjangoFilterBackend]
    # filterset_class = MovieFilter
    # pagination_class= Custompagination



class Movies_Details_view(generics.RetrieveUpdateDestroyAPIView):
    queryset= Movies_model.objects.all()
    serializer_class= Movie_serializer
    permission_classes=[IsAuthenticated,]  #IsAdminorReadonly
    # lookup_field= 'pk'




class Review_View(viewsets.ModelViewSet):
    queryset=  Review_Model.objects.all()
    serializer_class=Review_serializer
    permission_classes=[IsAuthenticated,]  #IsOwnerOrReadOnly

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        user= self.request.user
        movie= serializer.validated_data['Review_Movie_name']


        if Review_Model.objects.filter(Review_Movie_name=movie, user=user).exists():
            raise ValidationError('you have already reviewd this movie only you can delete or edit now')
        

        serializer.save(user=user)




class Review_Details_view(generics.RetrieveUpdateDestroyAPIView):
    queryset= Review_Model.objects.all()
    serializer_class= Review_serializer 
    permission_classes=[IsAuthenticated,]   #IsOwnerOrReadOnly







#custom auth

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import login

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.objects.create_user(username=username, password=password)
#         login(request, user)
#         return redirect('home')
#     return render(request, 'register.html')


#this view is for download

logger= logging.getLogger(__name__)

class MovieDownload(APIView):
    def get(self, request, pk):
        try:
            movie= Movies_model.objects.get(pk=pk)
            logger.info(f"Downloading fole for movie: {movie}")
            response= FileResponse(movie.Movie_Upload.open(), as_attachment=True, filename=movie.Movie_Upload.name)
            return response
        except movie.DoesNotExist:
            raise Http404('movie not found')


