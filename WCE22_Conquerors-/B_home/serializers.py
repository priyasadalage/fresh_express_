from rest_framework import serializers
from .models import *

class broadcastSerializer(serializers.ModelSerializer):
    class Meta:
        model=broadcast
        fields='__all__'