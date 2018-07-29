# Generated by Django 2.0.7 on 2018-07-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occurence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('createdData', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('CONSTRUCTION', 'CONSTRUCTION'), ('SPECIAL_EVENT', 'SPECIAL_EVENT'), ('INCIDENT', 'INCIDENT'), ('WEATHER_CONDITION', 'WEATHER_CONDITION'), ('ROAD_CONDITION', 'ROAD_CONDITION')], max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
