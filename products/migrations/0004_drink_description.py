# Generated by Django 4.0.5 on 2022-06-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_drink_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
