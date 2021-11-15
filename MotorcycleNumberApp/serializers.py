from rest_framework import serializers

from .models import MotorcycleNumber, MotorcycleNumberApartmentOwner
from ApartmentOwnerApp.models import ApartmentOwner


class MotorcycleNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorcycleNumber
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'motorcycle_number']

        depth = 10


class MotorcycleNumberSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = MotorcycleNumberApartmentOwner
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'motorcycle_number']

        depth = 10


class MotorcycleNumberApartmentOwnerSerializer(serializers.ModelSerializer):
    motorcycle_number_id = MotorcycleNumberSerializer(read_only=True)

    class Meta:
        model = MotorcycleNumberApartmentOwner
        # fields = '__all__'
        fields = ['id', 'apartment_owner_id', 'motorcycle_number_id']

        depth = 10


class MotorcycleNumberApartmentOwnerSerializerSet(serializers.ModelSerializer):
    motorcycle_number_id = serializers.SlugRelatedField(queryset=MotorcycleNumber.objects.all(), slug_field='id')
    apartment_owner_id = serializers.SlugRelatedField(queryset=ApartmentOwner.objects.all(), slug_field='id')

    class Meta:
        model = MotorcycleNumber
        # fields = '__all__'
        fields = ['id', 'apartment_owner_id', 'motorcycle_number_id']

        depth = 10
