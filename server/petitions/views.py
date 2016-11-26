# django
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# models
from .models import UserInfo
from .models import Petition
from .models import PetitionLike
from .models import Poll
from .models import PollChoice
from .models import PollUserVote

# core
from core.views import _check_if_student
from core.views import hash_sha256


def index(request):
    pass

def check_student(request):
    if (request.method == 'POST') and request.is_ajax():
        return JsonResponse({
            'result': _check_if_student(
                user_id=request.POST.get('user_id'),
                user_pw=request.POST.get('user_pw')
            ),
            'message': 'successfully checked'
        })
    return JsonResponse({
        'result': False,
        'message': 'Not an POST/AJAX call'
    })


def is_voted(self, poll, user_id):
    if hash_sha256(user_id) in PollUserVote.objects.value_list('user_mixed').filter(poll=poll):
        return True
    return False
