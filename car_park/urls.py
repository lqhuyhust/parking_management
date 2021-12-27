from django.urls import path
from car_park import views

urlpatterns = [
    path('', views.CarParkList.as_view()),
    path('', views.CarParkCreate.as_view()),
    path('<int:pk>', views.CarParkDetail.as_view()),
    path('<int:pk>/book', views.BookCarPark.as_view()),
    path('search', views.SearchCarPark.as_view()),
    path('parking-slots/<int:car_park_id>', views.ParkingSlotList.as_view()),
]