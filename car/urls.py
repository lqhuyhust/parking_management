from django.urls import path
from car import views

urlpatterns = [
    path('<str:username>', views.CarDetail.as_view())
]