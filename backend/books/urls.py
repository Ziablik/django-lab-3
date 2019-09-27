from django.urls import path
from .views import *
from . import views

app_name = 'staff'

urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
    path('work-table/', WorkTable.as_view()),
    path('readers/', ReaderList.as_view()),
    path('reading-rooms/', ReadingRoomList.as_view()),
    path('educations/', EducationList.as_view()),
    path('book-reader/<int:pk>', BookReaderAdd.as_view()),
    #
    # path('copy/', CopyList.as_view()),
    # path('copy/<int:pk>/', CopyDetail.as_view()),
    #
    # path('rent/', RentList.as_view()),
    # path('rent/<int:pk>/', RentDetail.as_view()),
]