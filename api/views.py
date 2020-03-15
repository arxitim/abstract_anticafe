from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Account
from .serializers import accountSerializer


class GetAccountInfo(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        account = Account.objects.get(email=request.user.email)
        serialized = accountSerializer(account)
        return Response(serialized.data)
