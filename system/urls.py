from django.urls import path
from . import views
from django.views.decorators.cache import never_cache

app_name='system'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('room_list/', views.RoomListView, name='RoomList'),
    path('booking_list/', views.BookingList, name='BookingList'),
    path('book/<category>', views.BookingView.as_view(), name='BookingView'),
    path('booking/cancel/<pk>', views.CancelBookingView.as_view(), name='CancelBookingView'),
]

