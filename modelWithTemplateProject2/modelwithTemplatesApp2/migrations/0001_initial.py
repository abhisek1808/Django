# Generated by Django 3.2.11 on 2022-02-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bike_Brand', models.CharField(max_length=20)),
                ('Bike_Model', models.CharField(max_length=10)),
                ('Bike_Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_Brand', models.CharField(max_length=20)),
                ('Car_Model', models.CharField(max_length=10)),
                ('Car_Price', models.FloatField()),
                ('Car_image', models.ImageField(height_field=200, upload_to='', width_field=300)),
            ],
        ),
    ]
