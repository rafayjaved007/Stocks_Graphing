# Generated by Django 3.2.5 on 2021-07-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='us_500',
            field=models.FloatField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='us_tech_100',
            field=models.FloatField(max_length=30),
        ),
    ]