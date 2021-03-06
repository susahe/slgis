# Generated by Django 2.0.1 on 2018-02-06 15:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_remove_person_user'),
        ('gsdivision', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='villager',
            name='id',
        ),
        migrations.AddField(
            model_name='villager',
            name='person_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person.Person'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 5, 15, 46, 36, 57294), verbose_name='සේවය අවසන් කල දිනය '),
        ),
    ]
