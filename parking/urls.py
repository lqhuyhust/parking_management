from django.urls import path
from parking import views

urlpatterns = [
    path('<str:username>', views.ParkingList.as_view())
]