# Generated by Django 3.2.9 on 2021-12-02 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_security_car_park'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]