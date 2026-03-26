from django.urls import path
from .views import HotelListCreateView, ReservationCreateView

urlpatterns = [
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('reservation/', ReservationCreateView.as_view(), name='reservation-create'),
]
