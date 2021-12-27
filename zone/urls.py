from django.urls import path
from zone import views

urlpatterns = [
    path('', views.ZoneList.as_view())
]