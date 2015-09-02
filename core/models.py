from django.utils.translation import ugettext as _
from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    owner = models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')
    full_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
