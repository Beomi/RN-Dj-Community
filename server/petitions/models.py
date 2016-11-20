# Django
from django.db import models
from django.conf import settings


from ..core.models import TimeStampModel


class Petition(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    content = models.TextField()


