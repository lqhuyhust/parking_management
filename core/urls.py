from django.urls import path
from .views import  ChangePassword, AuthLoginWithJWT
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login', AuthLoginWithJWT.as_view()),
    path('change-password/<str:pk>', ChangePassword.as_view())
]