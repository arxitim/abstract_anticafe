from django.utils import timezone
from django.shortcuts import redirect
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Account, Table, TableBookingQueue
from .serializers import accountSerializer


class GetAccountInfo(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        account = Account.objects.get(email=request.user.email)
        serialized = accountSerializer(account)
        return Response(serialized.data)


class BookingNow(APIView):
    def post(self, request, table_id):
        if not request.user.is_authenticated:
            return redirect('login')

        table = Table.objects.all().get(pk=table_id)
        account = Account.objects.all().get(email=request.user.email)
        new_booking = TableBookingQueue.objects.create(table=table, account=account,
                                                       guests_count=3, dt_start=timezone.now(),
                                                       dt_end=timezone.now())
        return JsonResponse({"status": True})

