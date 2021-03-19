from rest_framework import serializers
from .models import BraeburnApple

class AppleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'image', 'added')
        model = BraeburnApple