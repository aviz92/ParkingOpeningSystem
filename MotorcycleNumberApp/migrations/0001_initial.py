# Generated by Django 3.0.7 on 2021-11-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotorcycleNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_dis', models.BooleanField(default=False, verbose_name='Enable/Disable')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=36, unique=True, verbose_name='Motorcycle number')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='Description')),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
    ]
