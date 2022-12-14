# Generated by Django 4.0.6 on 2022-08-10 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='broadcast',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.TextField()),
                ('format', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=100)),
                ('toAllFarmers', models.BooleanField(default=True)),
            ],
        ),
    ]
