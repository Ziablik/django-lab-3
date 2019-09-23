from django.urls import path
from .views import *

app_name = 'staff'

urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
    # path('book/<int:pk>/copy/', BookCopyList.as_view()),
    #
    # path('copy/', CopyList.as_view()),
    # path('copy/<int:pk>/', CopyDetail.as_view()),
    #
    # path('rent/', RentList.as_view()),
    # path('rent/<int:pk>/', RentDetail.as_view()),
]