# Generated by Django 3.1.7 on 2021-02-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_bookmark_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_title',
            field=models.CharField(help_text='Title', max_length=250),
        ),
    ]
