# Django
from django.db import models
from django.conf import settings


from ..core.models import TimeStampModel


class Petition(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Like(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    which_petition = models.ForeignKey(Petition)
    is_valid = models.BooleanField(default=False)



