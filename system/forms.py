from django import forms
from .models import Room, Booking, Cat
# from .views import check_availability

from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class AvailabilityForm(forms.Form):
    category = forms.CharField(max_length=100)
    check_in = forms.DateTimeField(input_formats='%Y-%m-%dT%H:%M', required=True)
    check_out = forms.DateTimeField(input_formats='%Y-%m-%dT%H:%M', required=True)
    people = forms.IntegerField(required=True)

# validators=[validate_book],
# def validate_book(self, value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _('%(value)s No room is available in the given duration'),
#             params={'value': value},
#          )


    # def clean(self):
    #     cleaned_data = super().clean()
    #     room_list = Room.objects.filter(room_category=cleaned_data.get('category'), people=cleaned_data.get('people'))
    #     available_rooms = []
    #     for room in room_list:
    #         if check_availability(room, cleaned_data.get('check_in'), cleaned_data.get('check_out')):
    #             available_rooms.append(room)
    #     if len(available_rooms) == 0:
    #         raise ValidationError("No room is available in the given duration")
    #     # return super().clean()

    # def clean(self):
    #     super(AvailabilityForm, self).clean()
    #     room_list = Room.objects.filter(room_category=self.cleaned_data.get('category'), people=self.cleaned_data.get('people'))
    #     available_rooms = []
    #     for room in room_list:
    #         if check_availability(room, self.cleaned_data.get('check_in'), self.cleaned_data.get('check_out')):
    #             available_rooms.append(room)
    #     if len(available_rooms) == 0:
    #         self.errors['check_in'] = self.error_class(['No room is available in the given duration'])
    #         raise ValidationError("No room is available in the given duration")
    #     return self.cleaned_data

def check_availability(room, check_in, check_out):
    avail_list=[]
    booking_list=Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
