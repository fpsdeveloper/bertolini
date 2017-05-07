# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-07 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='caso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('f', models.CharField(max_length=20)),
                ('jd', models.CharField(max_length=100, verbose_name='JD')),
                ('descripcion', models.CharField(max_length=200)),
                ('expediente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='juzgado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='siniestro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='caso',
            name='tribunal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artcontrol.juzgado'),
        ),
    ]
