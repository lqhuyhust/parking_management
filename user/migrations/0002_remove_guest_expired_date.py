# Generated by Django 3.2.9 on 2021-12-18 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='expired_date',
        ),
    ]