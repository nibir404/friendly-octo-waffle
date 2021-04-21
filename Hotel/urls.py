from django.urls import path
from .views import RoomListView, BookingList, BookingView, RoomDetailView
from . import views

app_name = "Hotel"

urlpatterns = [
    path('', views.index, name='index'),
    path('room_list/', RoomListView.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
]