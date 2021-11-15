from django.db import models

from ApartmentOwnerApp.models import ApartmentOwner


class CarNumber(models.Model):
    en_dis = models.BooleanField(verbose_name='Enable/Disable', default=True)

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, blank=True, null=True)

    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True, blank=True, null=True)

    name = models.CharField(verbose_name='Car number', blank=False, max_length=36, unique=True)

    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)

    car_number = models.CharField(verbose_name='Car Number', max_length=36, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name']


class CarNumberApartmentOwner(models.Model):
    apartment_owner_id = models.ForeignKey(ApartmentOwner, on_delete=models.SET_NULL, verbose_name='Apartment Owner', default=None, blank=True,
                                           null=True, related_name='rn_cars')
    car_number_id = models.ForeignKey(CarNumber, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ['car_number_id']
