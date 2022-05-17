# Generated by Django 4.0.3 on 2022-05-17 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('selectedFirtsPokemon', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('move1', models.CharField(max_length=100)),
                ('move2', models.CharField(max_length=100)),
                ('move3', models.CharField(max_length=100)),
                ('favorite', models.BooleanField(default=False)),
                ('srcImg', models.CharField(max_length=300)),
                ('srcImgBack', models.CharField(max_length=300)),
                ('hp', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.user')),
            ],
        ),
    ]
