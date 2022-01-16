from rest_framework import serializers
from .models import RandomUUID


class RandomUUIDSerializerOut(serializers.ModelSerializer):
    
    class Meta:
        model = RandomUUID
        fields = ('uuid', 'created_on',)


