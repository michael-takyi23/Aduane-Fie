from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Table, MenuItem
from .forms import BookingForm


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
    return render(request, 'register.html', {'form': form})

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
