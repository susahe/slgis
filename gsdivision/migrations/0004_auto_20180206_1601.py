# Generated by Django 2.0.1 on 2018-02-06 16:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gsdivision', '0003_auto_20180206_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gramasevadivision',
            name='gs_divsison',
        ),
        migrations.AddField(
            model_name='gramasevadivision',
            name='gs_divsect',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='gsdivision.DivisionSectOffice', verbose_name='ප්\u200dරාද්ශිය ලේකම් කොට්ඨාශය'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_district',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gsdivision.District', verbose_name='දිස්ත්\u200dරික්කය'),
        ),
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 5, 16, 1, 3, 474167), verbose_name='සේවය අවසන් කල දිනය '),
        ),
    ]
