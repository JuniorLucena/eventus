# -*- coding: utf-8 -*-

import os
from uuid import uuid4

from PIL import Image

from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext as _
from django.db import models


class Event(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    description = models.TextField(_('Description'))
    start_date = models.DateTimeField(_('Start Date'))
    end_date = models.DateTimeField(_('End Date'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


class Room(models.Model):
    location = models.CharField(_('Location'), max_length=100)

    def __unicode__(self):
        return self.location

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')


def unique_filename(instance, filename):
    return 'photos/speakers/{0}.png'.format(uuid4().hex)


class Speaker(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    bio = models.TextField(_('Bio'), blank=True, null=True)
    thumbnail = models.ImageField(upload_to=unique_filename, blank=True, null=True)

    def save(self, size=(300, 300)):
        super(Speaker, self).save()
        if self.thumbnail:
            filename = os.path.join(settings.MEDIA_ROOT, self.thumbnail.name)
            image = Image.open(filename)
            image.thumbnail(size, Image.ANTIALIAS)
            image.save(filename)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')


class TypeSession(models.Model):
    type = models.CharField(_('Type'), max_length=45)
    event = models.ForeignKey(Event, related_name='type_sessions')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name = _('Type Session')
        verbose_name_plural = _('Type Sessions')


class Session(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))
    preconditions = models.TextField(_('Precoditions'), blank=True, null=True)
    num_accents = models.PositiveIntegerField(_('Num Accents'), default=0)
    is_published = models.BooleanField(_('Publish'), default=True)
    # relations
    room = models.ForeignKey(Room, related_name='sessions')
    type = models.ForeignKey(TypeSession, related_name='sessions')
    speakers = models.ManyToManyField(to=Speaker, related_name='sessions')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Session')
        verbose_name_plural = _('Sessions')
        ordering = ['title', ]


class DateTimeSession(models.Model):
    session = models.ForeignKey(Session, related_name='datetime_sessions')
    start_session = models.DateTimeField(_('Start Session'))
    end_session = models.DateTimeField(_('End Session'))

    class Meta:
        verbose_name = _('DateTime Session')
        verbose_name_plural = _('DateTime Sessions')
        ordering = ['start_session', 'end_session']


class EntrySession(models.Model):
    ENTRY, WAIT = range(1, 3)

    ENTRY_TITLES = dict(entry=_('Entry'), wait=_('Wait'))

    ENTRY_CHOICES = ((ENTRY, 'entry'),
                     (WAIT, 'wait'))

    session = models.ForeignKey(Session, related_name='entry_session')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entry_session')
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    status = models.SmallIntegerField(_('Status'), choices=ENTRY_CHOICES)

    class Meta:
        verbose_name = _('Entry Session')
        verbose_name_plural = _('Entry Sessions')
        unique_together = ('session', 'user')


@receiver(pre_save, sender=Speaker)
def update_image_speaker(sender, instance, **kwargs):
    speaker = Speaker.objects.filter(pk=instance.id).first()

    if speaker and speaker.thumbnail and instance.thumbnail:
        os.remove(os.path.join(settings.MEDIA_ROOT, speaker.thumbnail.name))
