import datetime

from rest_framework import serializers

from .models import ValidationRequest


class ValidationRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidationRequest
        fields = (
            'id',
            'name',
            'surname',
            'data'
        )

    def create(self, validated_data):
        return ValidationRequest.objects.create(**validated_data, date_sent=datetime.datetime.now())
