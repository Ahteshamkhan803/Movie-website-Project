from django.forms import ValidationError
from Movie_App.models import Movies_model, Platforms_model,Review_Model
from Movie_App.api.serializers import Movies_Serializer,Platforms_Serializer,Review_Serializer
from rest_framework import generics,viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from Movie_App.api.permission import IsOwnerOrSuperuserOrReadOnly
# from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend 
from Movie_App.api.filters import Movies_Filter
# from Movie_App.api.pagination import Custompagination
from django.http import FileResponse, Http404
from rest_framework.views import APIView
import logging




class Platform_view(generics.ListCreateAPIView):
    queryset= Platforms_model.objects.all()
    serializer_class= Platforms_Serializer





class movies_view(generics.ListCreateAPIView):
    queryset= Movies_model.objects.all()
    serializer_class= Movies_Serializer
    permission_classes=[AllowAny]   #,IsAdminorReadonly
    filter_backends=[DjangoFilterBackend]
    filterset_class = Movies_Filter
    # pagination_class= Custompagination



class Movies_Details_view(generics.RetrieveUpdateDestroyAPIView):
    queryset= Movies_model.objects.all()
    serializer_class= Movies_Serializer
    permission_classes=[IsAuthenticated] 
    # lookup_field= 'pk'




class Review_View(viewsets.ModelViewSet):
    queryset = Review_Model.objects.all()
    serializer_class = Review_Serializer
    permission_classes = [IsAuthenticated,IsOwnerOrSuperuserOrReadOnly]  




    def get_queryset(self):
        user= self.request.user
        return Review_Model.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        movies = serializer.validated_data['Review_Movie_name']

        if Review_Model.objects.filter(Review_Movie_name=movies, user=user).exists():
            raise ValidationError('You have already reviewed this movie. You can only edit or delete your review now.')

        serializer.save(user=user)



class Review_Details_view(generics.RetrieveUpdateDestroyAPIView):
    queryset= Review_Model.objects.all()
    serializer_class= Review_Serializer 
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


