from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Booking, Table, MenuItem
from .forms import BookingForm
from django.utils import timezone
from django.views.generic import UpdateView
from django.urls import reverse_lazy



# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # Logic to assign a table based on availability
            available_table = Table.objects.filter(capacity__gte=booking.guests).exclude(
                booking__date=booking.date,
                booking__time=booking.time
            ).first()
            if available_table:
                booking.table = available_table
                booking.save()
                messages.success(request, 'Booking created successfully!')
                return redirect('my_bookings')
            else:
                messages.error(request, 'No tables available for the selected date and time.')
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking cancelled successfully!')
        return redirect('my_bookings')
    return render(request, 'cancel_booking.html', {'booking': booking})

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'booking_detail.html', {'booking': booking})    

@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            updated_booking.user = request.user
            # Check if the new date and time are available for the booking
            available_table = Table.objects.filter(
                capacity__gte=updated_booking.guests
            ).exclude(
                booking__date=updated_booking.date,
                booking__time=updated_booking.time
            ).first()

            if available_table:
                updated_booking.table = available_table
                updated_booking.save()
                messages.success(request, 'Booking updated successfully!')
                return redirect('my_bookings')
            else:
                messages.error(request, 'No tables available for the selected date and time.')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'update_booking.html', {'form': form, 'booking': booking})

