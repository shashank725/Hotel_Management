from django import forms
from .models import Room, Booking

class AvailabilityForm(forms.Form):
    categories = {
        ('STD', 'Standard'), ('CR', 'Connecting Room'), ('DEL', 'Deluxe'), ('KIN', 'King'), ('QUE', 'Queen'),
        ('SUI', 'Suite'), ('PEN', 'Penthouse')
    }
    room_category = forms.ChoiceField(choices=categories, required=True)
    check_in = forms.DateTimeField(input_formats='%Y-%m-%dT%H:%M', required=True)
    check_out = forms.DateTimeField(input_formats='%Y-%m-%dT%H:%M', required=True)