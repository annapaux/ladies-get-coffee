# Generated by Django 3.0.5 on 2020-04-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200422_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
