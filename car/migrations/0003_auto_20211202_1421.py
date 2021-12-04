# Generated by Django 3.2.9 on 2021-12-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='cars'),
        ),
        migrations.AddField(
            model_name='car',
            name='license_plate',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_registration',
            field=models.ImageField(null=True, upload_to='car-registrations'),
        ),
    ]