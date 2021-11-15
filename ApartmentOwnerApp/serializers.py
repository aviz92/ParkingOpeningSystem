from rest_framework import serializers

from .models import ApartmentOwner

from ApartmentNumberApp.models import ApartmentNumberApartmentOwner
from ApartmentNumberApp.serializers import ApartmentNumberApartmentOwnerSerializer

from CarNumberApp.models import CarNumberApartmentOwner
from CarNumberApp.serializers import CarNumberApartmentOwnerSerializer

from MotorcycleNumberApp.models import MotorcycleNumberApartmentOwner
from MotorcycleNumberApp.serializers import MotorcycleNumberApartmentOwnerSerializer


class ApartmentOwnerSerializer(serializers.ModelSerializer):
    rn_apartments = ApartmentNumberApartmentOwnerSerializer(many=True, required=False)
    rn_cars = CarNumberApartmentOwnerSerializer(many=True, required=False)
    rn_motorcycles = MotorcycleNumberApartmentOwnerSerializer(many=True, required=False)

    class Meta:
        model = ApartmentOwner
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description',

                  'rn_apartments',
                  'rn_cars',
                  'rn_motorcycles',
                  ]

        depth = 10


class ApartmentOwnerSerializerSet(serializers.ModelSerializer):
    rn_apartments = serializers.SlugRelatedField(queryset=ApartmentNumberApartmentOwner.objects.all(), slug_field='id', many=True, required=False)
    rn_cars = serializers.SlugRelatedField(queryset=CarNumberApartmentOwner.objects.all(), slug_field='id', many=True, required=False)
    rn_motorcycles = serializers.SlugRelatedField(queryset=MotorcycleNumberApartmentOwner.objects.all(), slug_field='id', many=True, required=False)

    class Meta:
        model = ApartmentOwner
        # fields = '__all__'
        fields = ['id', 'en_dis', 'created_at', 'updated_at', 'name', 'description',

                  'rn_apartments',
                  'rn_cars',
                  'rn_motorcycles',
                  ]

        depth = 10
