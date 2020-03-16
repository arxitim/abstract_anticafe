from django.urls import path, re_path, include
from .views import GetAccountInfo, BookingNow

urlpatterns = [
    path('account_info/', GetAccountInfo.as_view(), name='account_info'),
    path('booking_now/<int:table_id>', BookingNow.as_view(), name='booking_now')
]