from django.urls import path
from .views import  ChangePassword, AuthLoginWithJWT

urlpatterns = [
    path('login/', AuthLoginWithJWT.as_view()),
    path('change-password/<int:pk>/', ChangePassword.as_view())
]