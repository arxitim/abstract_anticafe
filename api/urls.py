from django.urls import path, re_path, include
from .views import GetAccountInfo

urlpatterns = [
    path('account_info/', GetAccountInfo.as_view(), name='account_info'),
]