from django.urls import path
from .views import All_Reservation

urlpatterns = [
    path('reservations/', All_Reservation, name="reservations"),
]