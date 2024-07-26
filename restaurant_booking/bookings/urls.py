from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]