from django.urls import path
from car_park import views

urlpatterns = [
    path('', views.CarParkList.as_view()),
    path('<int:pk>', views.CarParkDetail.as_view()),
    path('<int:pk>/book', views.BookCarPark.as_view()),
    path('<int:pk>/follow', views.FollowCarPark.as_view()),
    path('search', views.SearchCarPark.as_view()),
    path('parking-slots', views.ParkingSlotList.as_view()),
    path('parking-slots/<int:pk>', views.ParkingSlotDetail.as_view()),
    path('ports', views.PortList.as_view()),
    path('ports/<int:pk>', views.PortDetail.as_view()),
]