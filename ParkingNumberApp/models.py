from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class ParkingNumber(models.Model):
    en_dis = models.BooleanField(verbose_name='Enable/Disable', default=True)

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, blank=True, null=True)

    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True, blank=True, null=True)

    name = models.CharField(verbose_name='Parking number', blank=False, max_length=36, unique=True)

    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)

    parking_number = models.IntegerField(verbose_name='Parking Number', blank=True, null=True, default=1,
                                         validators=[MinValueValidator(1), MaxValueValidator(99999)])

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['name'], ['parking_number']]
