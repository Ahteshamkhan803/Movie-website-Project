from django.urls import path, include
from User_Auth_App.api.views import Register_view,LoginView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
   path('register/',Register_view.as_view(), name='register'),
   path('login/', LoginView.as_view(), name='login'),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]