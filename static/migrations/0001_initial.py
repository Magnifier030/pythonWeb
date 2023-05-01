# Generated by Django 4.2 on 2023-04-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Water_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reservoir_id', models.IntegerField()),
                ('WaterLevel', models.FloatField()),
                ('EffectiveWaterStorageCapacity', models.FloatField()),
                ('Reservoir_name', models.CharField(max_length=50)),
            ],
        ),
    ]
