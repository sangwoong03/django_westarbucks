# Generated by Django 4.0.5 on 2022-06-03 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_allergy_allergy_drink_drink_image_nutrition_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='name',
        ),
    ]
