# Generated by Django 3.1.7 on 2021-02-24 00:23

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, null=True),
        ),
    ]