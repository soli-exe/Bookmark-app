# Generated by Django 3.1.7 on 2021-02-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20210222_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_publication_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_title',
            field=models.CharField(max_length=250),
        ),
    ]
