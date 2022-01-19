from django.urls import path
from payment import views

urlpatterns = [
    path('checkout/<int:pk>', views.Checkout.as_view(), name='checkout'),
    path('success', views.Success.as_view(), name='success'),
    path('failure', views.Failure.as_view(), name='failure'),
]