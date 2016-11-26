from django.contrib import admin

from .models import *

admin.site.register(Petition)
admin.site.register(PetitionLike)
admin.site.register(UserInfo)
admin.site.register(Poll)
admin.site.register(PollChoice)
admin.site.register(PollUserVote)