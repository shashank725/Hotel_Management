from django.urls import path
from . import views

app_name='system'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sights/', views.sights, name='sights'),
]

"""path('/bookings', views.BookingView.as_view() , name='bookings' ),"""