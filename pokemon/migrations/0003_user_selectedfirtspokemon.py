# Generated by Django 4.0.3 on 2022-05-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='selectedFirtsPokemon',
            field=models.BooleanField(default=False),
        ),
    ]
