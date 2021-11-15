from rest_framework import serializers

from .models import CarNumber, CarNumberApartmentOwner
from ApartmentOwnerApp.models import ApartmentOwner


class CarNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarNumber
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'car_number']

        depth = 10


class CarNumberSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = CarNumber
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'car_number']

        depth = 10


class CarNumberApartmentOwnerSerializer(serializers.ModelSerializer):
    car_number_id = CarNumberSerializer(read_only=True)

    class Meta:
        model = CarNumberApartmentOwner
        # fields = '__all__'
        fields = ['id', 'apartment_owner_id', 'car_number_id']

        depth = 10


class CarNumberApartmentOwnerSerializerSet(serializers.ModelSerializer):
    car_number_id = serializers.SlugRelatedField(queryset=CarNumber.objects.all(), slug_field='id')
    apartment_owner_id = serializers.SlugRelatedField(queryset=ApartmentOwner.objects.all(), slug_field='id')

    class Meta:
        model = CarNumberApartmentOwner
        # fields = '__all__'
        fields = ['id', 'apartment_owner_id', 'car_number_id']

        depth = 10
