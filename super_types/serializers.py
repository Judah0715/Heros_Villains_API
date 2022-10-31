from dataclasses import field
from importlib.metadata import files
from rest_framework import serializers
from . import models
from.models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['type']