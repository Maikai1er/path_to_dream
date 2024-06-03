from rest_framework import serializers
from .models import CustomUser
from dreams.serializers import DreamSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    dreams = DreamSerializer(many=True, read_only=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'dreams']
