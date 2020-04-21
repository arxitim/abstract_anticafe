from django.urls import path, re_path, include

from staff.views import *


urlpatterns = [
    path('<int:booking_id>', ConfirmBooking.as_view(), name='confirm_booking'),
]
