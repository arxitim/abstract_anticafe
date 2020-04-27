from django.urls import path, re_path, include
from .views import GetAccountInfo, DeleteBooking

urlpatterns = [
    path('account_info/', GetAccountInfo.as_view(), name='account_info'),
    path('delete_booking/<int:booking_id>', DeleteBooking.as_view()),
]
