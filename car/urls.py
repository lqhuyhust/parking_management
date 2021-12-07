from django.urls import path
from car import views

urlpatterns = [
    path('', views.CarList.as_view()),
    path('<str:username>', views.CarDetail.as_view()),
]