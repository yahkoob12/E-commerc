# Generated by Django 5.0.2 on 2024-03-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
