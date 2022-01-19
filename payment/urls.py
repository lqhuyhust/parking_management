from django.urls import path
from payment import views

urlpatterns = [
    path('checkout/<int:pk>', views.Checkout.as_view(), name='checkout'),
    path('success/<str:pk>', views.Success.as_view(), name='success'),
    path('failure/<str:pk>', views.Failure.as_view(), name='failure'),
]