# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-18 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategorija', to='evidencija.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdOsobe', models.CharField(max_length=100)),
                ('PrezimeOsobe', models.CharField(max_length=20)),
                ('ImeOsobe', models.CharField(max_length=20)),
                ('OIB', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='UlogaOsobe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SifProjekta', models.CharField(max_length=100)),
                ('IdUloge', models.CharField(max_length=100)),
                ('DatDodjele', models.TextField()),
                ('IdOsobe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uloga', to='evidencija.Category')),
            ],
        ),
    ]