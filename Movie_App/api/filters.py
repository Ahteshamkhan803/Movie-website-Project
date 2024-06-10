import django_filters
from Movie_App.models import Movies_model




class Movies_Filter(django_filters.FilterSet):
    class Meta:
        model= Movies_model
        fields= {
            'Movie_Name': ['icontains','istartswith'],
        }

