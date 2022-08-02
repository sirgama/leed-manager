from dataclasses import fields
from rest_framework import serializers
from .models import Leed

class LeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leed
        fields = '__all__'