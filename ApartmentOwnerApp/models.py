from django.db import models


class ApartmentOwner(models.Model):
    en_dis = models.BooleanField(verbose_name='Enable/Disable', default=True)

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, blank=True, null=True)

    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True, blank=True, null=True)

    name = models.CharField(verbose_name='Owner number', blank=False, max_length=36, unique=True)

    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name']
