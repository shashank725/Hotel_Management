from django import forms
from .models import Room, Booking, Cat
# from .views import check_availability

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class AvailabilityForm(forms.Form):
    category = forms.CharField(max_length=100)
    check_in = forms.DateTimeField(input_formats='%Y-%m-%dT%H:%M', required=True)
    check_out = forms.DateTimeField(input_formats='%Y-%m-%dT%H:%M', required=True)
    people = forms.IntegerField(required=True)

# validators=[validate_book],
# def validate_book(value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _('%(value)s No room is available in the given duration'),
#             params={'value': value},
#          )


    # def clean_recipients(self, category):
    #     print('form='category)
    #     data = self.cleaned_data
    #     room_list = Room.objects.filter(room_category=category, people=data['people'])
    #     available_rooms = []
    #     for room in room_list:
    #         if check_availability(room, data['check_in'], data['check_out']):
    #             available_rooms.append(room)
    #     if len(available_rooms) == 0:
    #         raise ValidationError("No room is available in the given duration")

    # def clean(self, category):
    #     print('form='category)
    #     room_list = Room.objects.filter(room_category=category, people=self.people)
    #     available_rooms = []
    #     for room in room_list:
    #         if check_availability(room, self.check_in, self.check_out):
    #             available_rooms.append(room)
    #     if len(available_rooms) == 0:
    #         raise ValidationError('No room is available in the given duration')
    #     return super().clean(category)
