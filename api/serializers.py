from rest_framework import serializers
from core.models import Account


class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
