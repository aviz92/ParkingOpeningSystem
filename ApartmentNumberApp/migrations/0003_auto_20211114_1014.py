# Generated by Django 3.0.7 on 2021-11-14 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApartmentNumberApp', '0002_auto_20211114_1010'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='apartmentnumber',
            unique_together={('apartment_number',), ('name',)},
        ),
    ]
