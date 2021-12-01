from django.urls import path
from car import views

urlpatterns = [
    path('', views.CarList.as_view()),
    path('/<int:pk>', views.CarDetail.as_view()),
]