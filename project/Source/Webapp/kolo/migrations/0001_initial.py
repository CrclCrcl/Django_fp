# Generated by Django 3.2.18 on 2023-04-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('surname', models.CharField(max_length=500)),
                ('mail_adress', models.CharField(max_length=1000)),
                ('creation_date', models.DateTimeField()),
                ('modification_date', models.DateTimeField()),
            ],
        ),
    ]