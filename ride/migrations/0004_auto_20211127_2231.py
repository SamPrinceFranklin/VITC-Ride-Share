# Generated by Django 3.2.9 on 2021-11-27 17:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_alter_ridehost_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='ridehost',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='ridehost',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
