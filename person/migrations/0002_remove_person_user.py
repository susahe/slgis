# Generated by Django 2.0.1 on 2018-02-06 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
    ]
