from django.urls import path
from user import views

urlpatterns = [
    path('guests', views.GuestList.as_view()),
    path('guests/<int:pk>', views.GuestDetail.as_view()),
    path('securities', views.SecurityList.as_view()),
    path('securities/<int:pk>', views.SecurityDetail.as_view()),
    path('guest-types', views.GuestTypeList.as_view()),
    path('guest-types/<int:pk>', views.GuestTypeDetail.as_view()),
]