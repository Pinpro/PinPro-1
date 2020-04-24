# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-04-24 10:10
from __future__ import unicode_literals

import core.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', max_length=255, upload_to=core.utils.upload_path, width_field='width')),
                ('height', models.PositiveIntegerField(default=0, editable=False)),
                ('width', models.PositiveIntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', max_length=255, upload_to=core.utils.upload_path, width_field='width')),
                ('size', models.CharField(max_length=100)),
                ('height', models.PositiveIntegerField(default=0, editable=False)),
                ('width', models.PositiveIntegerField(default=0, editable=False)),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_images.Image')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='thumbnail',
            unique_together=set([('original', 'size')]),
        ),
    ]
