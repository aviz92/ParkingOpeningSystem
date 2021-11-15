from rest_framework import serializers

from .models import ApartmentNumber, ApartmentNumberApartmentOwner
from ApartmentOwnerApp.models import ApartmentOwner


class ApartmentNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentNumber
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'apartment_number', 'parking_number', 'parking_count',

                  'get_amount_of_parking'
                  ]

        depth = 10


class ApartmentNumberSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = ApartmentNumber
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description', 'apartment_number', 'parking_number', 'parking_count',

                  'get_amount_of_parking'
                  ]

        depth = 10


class ApartmentNumberApartmentOwnerSerializer(serializers.ModelSerializer):
    apartment_number_id = ApartmentNumberSerializer(read_only=True)

    class Meta:
        model = ApartmentNumberApartmentOwner
        # fields = '__all__'
        fields = ['id', 'apartment_owner_id', 'apartment_number_id']

        depth = 0


class ApartmentNumberApartmentOwnerSerializerSet(serializers.ModelSerializer):
    apartment_number_id = serializers.SlugRelatedField(queryset=ApartmentNumber.objects.all(), slug_field='id')
    apartment_owner_id = serializers.SlugRelatedField(queryset=ApartmentOwner.objects.all(), slug_field='id')

    class Meta:
        model = ApartmentNumberApartmentOwner
        # fields = '__all__'
        fields = ['id', 'apartment_owner_id', 'apartment_number_id']

        depth = 0
