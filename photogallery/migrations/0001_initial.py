# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=140)),
                ('location', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='photo')),
                ('caption', models.TextField()),
                ('date', models.DateField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', blank=True, verbose_name='Tags', through='taggit.TaggedItem')),
            ],
        ),
    ]
