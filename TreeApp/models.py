from django.db import models

from mptt.models import TreeForeignKey, MPTTModel
from django.core.validators import MaxValueValidator, MinValueValidator

from ApartmentNumberApp.models import ApartmentNumber


class LeveledTree(MPTTModel):
    name = models.CharField(verbose_name='Name', blank=False, max_length=256, null=True)

    apartment_number = models.ForeignKey(ApartmentNumber, on_delete=models.SET_NULL, verbose_name='Setup name', default=None, blank=True, null=True)
    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)
    parent = TreeForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['name'], ['apartment_number']]


class Categories(models.Model):
    category_name = models.CharField(max_length=999, null=True)
    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)

    def __str__(self):
        return self.category_name

    class Meta:
        unique_together = ['category_name']


class Parameters(models.Model):
    variable_name = models.CharField(max_length=999, null=True)
    variable_category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)

    def __str__(self):
        return self.variable_name

    class Meta:
        unique_together = ['variable_name']
        ordering = ['variable_name']


class ParametersTree(models.Model):
    variable_name = models.ForeignKey(Parameters, on_delete=models.CASCADE, default=None)
    variable_value = models.CharField(max_length=255, null=True)
    fk = models.ForeignKey(LeveledTree, on_delete=models.CASCADE, default=None,  related_name='parameters_leveled_tree')
    description = models.TextField(verbose_name='Description', blank=True, max_length=5000)

    def __str__(self):
        return self.variable_value

    class Meta:
        unique_together = ['fk', 'variable_name']
