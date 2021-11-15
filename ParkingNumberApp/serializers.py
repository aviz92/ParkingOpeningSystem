from rest_framework import serializers

from .models import ParkingNumber


class ParkingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingNumber
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'parking_number']

        depth = 10


class ParkingNumberSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = ParkingNumber
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'parking_number']

        depth = 10
