# Generated by Django 3.2.9 on 2021-12-02 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_guest_expired_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='guest_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='guest_type', to='user.guesttype'),
        ),
    ]