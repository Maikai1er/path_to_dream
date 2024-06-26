from rest_framework import serializers
from .models import Dream
from steps_to_dream.serializers import StepSerializer


class DreamSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Dream
        fields = '__all__'
