from django.urls import path
from payment import views

urlpatterns = [
    path('checkout/<int:pk>', views.Checkout.as_view(), name='checkout'),
    path('success', views.success, name='success'),
    path('failure', views.failure, name='failure'),
]