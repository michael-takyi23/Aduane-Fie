from django.urls import path
from . import views
from .views import update_booking

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('register/', views.register, name='register'),
    path('booking/update/<int:booking_id>/', update_booking, name='update_booking'),
]

