# Generated by Django 3.0.5 on 2020-04-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200423_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]