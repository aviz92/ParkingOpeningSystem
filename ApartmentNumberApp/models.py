from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from ApartmentOwnerApp.models import ApartmentOwner
from ParkingNumberApp.models import ParkingNumber


class ApartmentNumber(models.Model):
    en_dis = models.BooleanField(verbose_name='Enable/Disable', default=True)

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, blank=True, null=True)

    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True, blank=True, null=True)

    name = models.CharField(verbose_name='Apartment number', blank=False, max_length=36, unique=True)

    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)

    apartment_number = models.IntegerField(verbose_name='Apartment Number', null=True, default=1,
                                           validators=[MinValueValidator(1), MaxValueValidator(99999)])

    parking_number = models.ManyToManyField(ParkingNumber, verbose_name='Parking Number', default=None,
                                            related_name='rn_apartment_number_parking_number')

    parking_count = models.IntegerField(verbose_name='Parking Count', null=True, default=0,
                                        validators=[MinValueValidator(0), MaxValueValidator(99999)])

    def get_amount_of_parking(self):
        return len(self.parking_number.values())

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['name'], ['apartment_number']]


class ApartmentNumberApartmentOwner(models.Model):
    apartment_owner_id = models.ForeignKey(ApartmentOwner, on_delete=models.SET_NULL, verbose_name='Apartment Owner', default=None, blank=True,
                                           null=True, related_name='rn_apartments')
    apartment_number_id = models.ForeignKey(ApartmentNumber, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ['apartment_owner_id', 'apartment_number_id']
