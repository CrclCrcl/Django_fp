# Generated by Django 3.2.18 on 2023-04-24 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kolo', '0003_auto_20230424_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='modification_date',
        ),
    ]
