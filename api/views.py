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


class DeleteBooking(APIView):
    def get(self, request, booking_id):
        return redirect('homePage')

    def delete(self, request, booking_id):
        if not request.user.is_authenticated:
            return redirect('login')

        try:
            booking = TableBookingQueue.objects.filter(pk=booking_id, account=request.user)[0]
            booking.delete()
        except IndexError:
            return JsonResponse({'status': False})

        return JsonResponse({'status': True})
