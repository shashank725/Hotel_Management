from django.urls import path
from . import views

app_name='system'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sights/', views.sights, name='sights'),
    path('room_list/', views.RoomList.as_view(), name='RoomList'),
    path('booking_list/', views.BookingList.as_view(), name='BookingList'),
    path('book/', views.BookingView.as_view(), name='booking_view'),
]

