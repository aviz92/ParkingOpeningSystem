# Generated by Django 3.0.7 on 2021-11-14 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApartmentOwnerApp', '0008_remove_apartmentowner_apartment_number'),
        ('ApartmentNumberApp', '0006_apartmentnumberapartmentowner'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='apartmentnumberapartmentowner',
            unique_together={('apartment_owner_id', 'apartment_number_id')},
        ),
    ]
