# Generated by Django 3.2.9 on 2021-12-07 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20211203_1128'),
        ('car', '0003_auto_20211202_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='guest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='user.guest'),
        ),
    ]
