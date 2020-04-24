# Generated by Django 3.0.5 on 2020-04-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200424_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='current_job',
            field=models.CharField(blank=True, default='', help_text='Current job or status (e.g. software engineer, student, entrepreneur)', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, default='', help_text='Provide an email peers can reach you at.', max_length=50),
        ),
    ]
