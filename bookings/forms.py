from django import forms
from django.utils import timezone
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now().date():
            raise forms.ValidationError("The booking date cannot be in the past.")
        return date

    def clean_time(self):
        date = self.cleaned_data.get('date')
        time = self.cleaned_data.get('time')
        if date == timezone.now().date() and time < timezone.now().time():
            raise forms.ValidationError("The booking time cannot be in the past.")
        return time    