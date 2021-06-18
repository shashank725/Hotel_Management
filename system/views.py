from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Booking, Room
from .forms import AvailabilityForm
import datetime


# Create your views here.

def homepage(request):
    return render(request, 'system/index.html')

@never_cache
def RoomListView(request):
    room=Room.objects.all()[0]
    room_categories=dict(room.categories)
    # print(room_categories)
    room_values=room_categories.values()
    # print('cat=', room_values)
    room_list=[]
    for room_category in room_categories:
        room=room_categories.get(room_category)
        # print(room)
        room_url=reverse('system:BookingView', kwargs={'category':room_category})
        # print(room_url)
        room_list.append((room, room_url))
    context={
        'room_list':room_list,
    }
    # print(room_list)
    return render(request, 'system/room_list.html', context)

"""
class BookingView(generic.FormView):
    form_class = AvailabilityForm
    template_name = 'system/book.html'
    success_url = 'system:BookingList'

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
            return HttpResponse(booking)
        else:
            return HttpResponse('This category of rooms are booked.')
"""

class BookingView(generic.View):
    def get(self, request, *args, **kwargs):
        category=self.kwargs.get('category', None)
        form=AvailabilityForm()
        room_list=Room.objects.filter(category=category)
        if len(room_list)>0:
            room=room_list[0]
            room_category=dict(room.categories).get(room.category, None)
            context = {
                'room_category': room_category,
                'form':form,
            }
            return render(request, 'system/book.html', context)
        else:
            return HttpResponse('Category does not exit !')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form=AvailabilityForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user, room=room, check_in=data['check_in'], check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This category of rooms are booked.')

class BookingList(generic.ListView):
    model = Booking
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list=Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list

class CancelBookingView(generic.DeleteView):
    model = Booking
    template_name = 'system/booking_cancel_view.html'
    success_url = reverse_lazy('system:RoomList')





def check_availability(room, check_in, check_out):
    avail_list=[]
    booking_list=Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)