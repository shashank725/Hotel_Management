from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Booking, Room
from .forms import AvailabilityForm
import datetime

# Create your views here.

def homepage(request):
    return render(request, 'system/index.html')

def sights(request):
    return render(request, 'system/sights.html')

class RoomList(generic.ListView):
    model = Room

class BookingList(generic.ListView):
    model = Booking

class BookingView(generic.FormView):
    form_class = AvailabilityForm
    template_name = 'system/availability_form.html'

    def form_valid(self, form):
        data=form.cleaned_data
        room_list=Room.objects.filter(category=data['room_category'])
        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room=available_rooms[0]
            booking=Booking.objects.create(
                user=self.request.user, room=room, check_in=data['check_in'], check_out=data['check_out']
            )
            booking.save()
            return HttpResponse("Booked")
        else:
            return HttpResponse('This category of rooms are booked.')




def check_availability(room, check_in, check_out):
    avail_list=[]
    booking_list=Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
        return all(avail_list)