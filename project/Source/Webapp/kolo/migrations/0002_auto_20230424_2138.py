# Generated by Django 3.2.18 on 2023-04-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kolo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='modification_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
