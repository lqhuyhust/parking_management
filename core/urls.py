from django.urls import path
from .views import  ChangePassword
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('change-password/<int:pk>/', ChangePassword.as_view())
]