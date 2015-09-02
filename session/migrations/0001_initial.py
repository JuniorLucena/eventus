# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import session.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DateTimeSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_session', models.DateTimeField()),
                ('end_session', models.DateTimeField()),
            ],
            options={
                'ordering': ['start_session', 'end_session'],
                'verbose_name': 'DateTime Session',
                'verbose_name_plural': 'DateTime Sessions',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('owner', models.ForeignKey(related_name='event', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('preconditions', models.TextField(null=True, verbose_name='Precoditions', blank=True)),
                ('num_accents', models.PositiveIntegerField(default=0, verbose_name='Num Accents')),
                ('room', models.ForeignKey(related_name='sessions', to='session.Room')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('bio', models.TextField(null=True, verbose_name='Bio', blank=True)),
                ('thumbnail', models.ImageField(null=True, upload_to=session.models.unique_filename, blank=True)),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
        ),
        migrations.CreateModel(
            name='TypeSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=45, verbose_name='Type')),
                ('event', models.ForeignKey(related_name='type_sessions', to='session.Event')),
            ],
            options={
                'verbose_name': 'Type Session',
                'verbose_name_plural': 'Type Sessions',
            },
        ),
        migrations.AddField(
            model_name='session',
            name='speakers',
            field=models.ManyToManyField(related_name='sessions', to='session.Speaker'),
        ),
        migrations.AddField(
            model_name='session',
            name='type',
            field=models.ForeignKey(related_name='sessions', to='session.TypeSession'),
        ),
        migrations.AddField(
            model_name='datetimesession',
            name='session',
            field=models.ForeignKey(related_name='datetime_sessions', to='session.Session'),
        ),
    ]
