from django.urls import path
from .views import HotelListView, ReservationCreateView

urlpatterns = [
    path('hotels/', HotelListView.as_view()),
    path('reservation/', ReservationCreateView.as_view()),
]