from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, render, redirect, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Booking, Room, Cat
from .forms import AvailabilityForm
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
# Payment
from hotel import settings
import razorpay
razorpay_client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_account_id))
razorpay_client.set_app_details({"title" : "Django", "version" : "3.2.3"})

# Create your views here.
@never_cache
def homepage(request):
    return render(request, 'system/index.html')


@login_required
def RoomListView(request):
    # cat_room_list=[]
    # for i in range(0,7):
    #     cat_room_list.append(Cat.objects.all()[i])
    # # print(cat_room_list)
    cat_room_list=Cat.objects.all()
    cat_list = []
    for cat in cat_room_list:
        # print(cat)
        cat_url = reverse('system:explore', kwargs={'category':cat})
        cat_list.append((cat,cat_url))
    context = {'cat_list':cat_list,}
    return render(request, 'system/room_list.html', context)
    # room=Room.objects.all()[0]
    # room_categories=dict(room.categories)
    # room_values=room_categories.values()
    # room_list=[]
    # for room_category in room_categories:
    #     room=room_categories.get(room_category)
    #     room_url=reverse('system:BookingView', kwargs={'category':room_category})
    #     room_list.append((room, room_url))
    # context={
    #     'room_list':room_list,
    # }
    # return render(request, 'system/room_list.html', context)

class Explore(generic.View):
    def get(self, request, *args, **kwargs):
        category=self.kwargs.get('category', None)
        form=AvailabilityForm()
        room_list=Room.objects.filter(room_category=category)
        print(room_list)
        cat = Cat.objects.filter(category=category)
        context={'category':category, 'cat':cat, 'room_list':room_list,}
        return render(request, 'system/explore.html', context)
        # if len(room_list)>0:
        #     room=room_list[0]
        #     room_category=dict(room.categories).get(room.category, None)
        #     context = {
        #         'room_category': room_category,
        #         'form':form,
        #     }
        #     return render(request, 'system/book.html', context)
        # else:
        #     return HttpResponse('Category does not exit !')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form=AvailabilityForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
        else:
            return HttpResponseRedirect(reverse('system:explore'))
        room_list = Room.objects.filter(room_category=category, people=data['people'])
        print(room_list)
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:
            room = available_rooms[0]
            print(category)
            # To get room amount
            # amt = Room.objects.all()[0]
            # amt_categories = dict(amt.categories_amount)
            # tamount = amt_categories.get(category)
            booking = Booking.objects.create(
                user=self.request.user, room=room, check_in=data['check_in'], check_out=data['check_out'], amount=100
            )
            booking.save()
            return HttpResponseRedirect(reverse('system:BookingList'))
        else:
            return HttpResponse('<h1>Sorry ! This room is not available.</h1><br><h2>Try booking another one.</h2>')


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
            print(room_category)
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
            print(category)
            # To get room amount
            amt = Room.objects.all()[0]
            amt_categories = dict(amt.categories_amount)
            tamount = amt_categories.get(category)
            booking = Booking.objects.create(
                user=self.request.user, room=room, check_in=data['check_in'], check_out=data['check_out'], amount=tamount
            )
            booking.save()

            order_currency = 'INR'

            # order_amount = tamount
            # order_currency = 'INR'
            # order_receipt = booking.order_id
            # print(booking.order_id)
            # notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL
            # razorpay_client.order.create(amount=tamount*100, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='0')

            # notes = {"address": "Glug, NIT Dgp"}
            # razorpay_order = razorpay_client.order.create(dict(amount=tamount*100, currency=order_currency, notes = notes, receipt=booking.order_id, payment_capture='0'))
            # print(razorpay_order)
            # booking.razorpay_order_id = razorpay_order['id']
            # print(razorpay_order['id'])
            # booking.save()
            # return render(request, 'system:BookingList')
            return HttpResponseRedirect(reverse('system:BookingList'))
        else:
            return HttpResponse('<h1>Sorry ! This room is not available.</h1><br><h2>Try booking another one.</h2>')


"""class BookingList(generic.ListView):
    model = Booking
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list=Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list"""

def BookingList(request):
    if request.method == 'GET':
        callback_url = 'http://'+ str(get_current_site(request))+"/booking_list/"
        print(callback_url)
        if request.user.is_staff:
            booking_list = Booking.objects.all()
            print(booking_list)
            context = {'booking_list':booking_list, 'callback_url':callback_url, 'settings_razorpay_id':settings.razorpay_id,}
            return render(request, 'system/booking_list.html', context)
        else:
            booking_list = Booking.objects.filter(user=request.user)
            context = {'booking_list':booking_list, 'callback_url':callback_url, 'settings_razorpay_id':settings.razorpay_id,}
            print(settings.razorpay_id)
            return render(request, 'system/booking_list.html', context)
    # if request.method == 'POST':
    #     try:
    #         payment_id = request.POST.get('razorpay_payment_id', '')
    #         order_id = request.POST.get('razorpay_order_id','')
    #         signature = request.POST.get('razorpay_signature','')
    #         params_dict = { 
    #         'razorpay_order_id': order_id, 
    #         'razorpay_payment_id': payment_id,
    #         'razorpay_signature': signature
    #         }
    #         try:
    #             order_db = Order.objects.get(razorpay_order_id=order_id)
    #         except:
    #            raise Http404


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
