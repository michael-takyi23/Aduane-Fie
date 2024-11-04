from django import forms
from django.utils import timezone
from .models import Booking

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