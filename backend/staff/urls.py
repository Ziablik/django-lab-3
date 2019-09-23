from django.urls import path
from .views import *

app_name = 'staff'

urlpatterns = [
    path('reader/', ReaderList.as_view()),
    path('reader/<int:pk>/', ReaderDetail.as_view()),

    path('room/', RoomList.as_view()),
]