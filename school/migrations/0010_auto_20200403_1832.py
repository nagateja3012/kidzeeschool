# Generated by Django 3.0.4 on 2020-04-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20200403_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='date',
            field=models.DateTimeField(max_length=255),
        ),
    ]
