from django.urls import path
from user import views

urlpatterns = [
    path('guests/register', views.Register.as_view()),
    path('guests/<str:username>', views.GuestDetail.as_view())
]