# Django
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User as django_User

# Python
from datetime import date

# Core
from core.models import TimeStampModel


class Petition(TimeStampModel):
    user = models.ForeignKey(django_User)
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField('PetitionLike', blank=True)

    def __str__(self):
        return self.title


class PetitionProgress(TimeStampModel):
    user = models.ForeignKey(django_User)


class PetitionLike(TimeStampModel):
    user = models.ForeignKey(django_User)
    which_petition = models.ForeignKey(Petition)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.which_petition.__str__() + ' : ' + str(self.is_valid)


class UserInfo(TimeStampModel):
    @staticmethod
    def this_year_0000():
        return (int(date.today().strftime('%Y')) + 1) * 10000  # this year's student id maximum, when 2016, 20170000

    user = models.OneToOneField(django_User)
    student_id = models.PositiveIntegerField(
        validators=[MaxValueValidator(this_year_0000()), MinValueValidator(20000000)],
        default=0
    )
    membership_until = models.DateField(blank=True, null=True)
    google_id_made = models.BooleanField(default=False)
    snue_p_updated = models.BooleanField(default=False)

    @property
    def is_student(self):
        if self.student_id != 0:
            return True
        return False

    @property
    def is_test_taker(self):
        if self.student_id > (self.this_year_0000() - 30000):
            return True
        return False

    def __str__(self):
        return self.user + ' : ' + self.student_id


class Poll(TimeStampModel):
    user = models.ForeignKey(django_User)
    title = models.CharField(max_length=255)
    contents = models.TextField()

    def __str__(self):
        return self.title


class PollChoice(TimeStampModel):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=255)

    def __str__(self):
        return self.poll.__str__() + ' : ' + self.choice


class PollUserVote(TimeStampModel):
    user_mixed = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(PollChoice)

    def __str__(self):
        return self.poll.__str__() + ' : ' + self.choice.choice
