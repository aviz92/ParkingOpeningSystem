# Generated by Django 3.0.7 on 2021-11-14 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ParkingNumberApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='parkingnumber',
            unique_together={('parking_number',), ('name',)},
        ),
    ]
