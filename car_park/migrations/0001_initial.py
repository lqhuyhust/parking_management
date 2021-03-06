# Generated by Django 3.2.9 on 2021-12-15 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.CharField(default='', max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('car_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_park.carpark')),
            ],
        ),
    ]
