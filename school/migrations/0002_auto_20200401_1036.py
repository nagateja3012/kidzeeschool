# Generated by Django 3.0.4 on 2020-04-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='payment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='receviable',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
