# Generated by Django 3.0.4 on 2020-04-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
