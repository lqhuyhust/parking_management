from django.urls import path
from parking import views

urlpatterns = [
    path('', views.ParkingList.as_view()),
    path('<int:pk>', views.ParkingDetail.as_view())
]