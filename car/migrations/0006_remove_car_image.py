# Generated by Django 3.2.9 on 2021-12-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20211210_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]
