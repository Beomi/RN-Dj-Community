# Django
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User as django_User

# Python
from datetime import date

# Core
from ..core.models import TimeStampModel


class Petition(TimeStampModel):
    user = models.ForeignKey(django_User)
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(Like, name='likes')

    def __str__(self):
        return self.title

    @property
    def how_many_likes(self):
        return self.


class Like(TimeStampModel):
    user = models.ForeignKey(django_User)
    which_petition = models.ForeignKey(Petition)
    is_valid = models.BooleanField(default=False)


class UserInfo(TimeStampModel):
    this_year_0000 = (int(date.today().strftime('%Y')) + 1) * 10000 # this year's student id maximum, when 2016, 20170000
    user = models.OneToOneField(django_User)
    student_id = models.PositiveIntegerField(
        validators=[MaxValueValidator(this_year_0000), MinValueValidator(20000000)],
        default=0
    )

    @property
    def is_student(self):
        if self.student_id != 0:
            return True
        return False


class Vote(TimeStampModel):
    user = models.ForeignKey(django_User)
    title = models.CharField(max_length=255)
    contents = models.TextField()
    likes = models.ManyToManyField(django_User)

    @property
    def check_liked(self, user_pk):
        if django_User.objects.get(pk=user_pk) in self.likes:
            return True
        else:
            return False