# django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# core
from ..core.views import _check_if_student


def index(request):
    pass

def check_student(request):
    if (request.method == 'POST') and request.is_ajax():
        return JsonResponse({
            'result': _check_if_student(
                user_id=request.POST.get('user_id'),
                user_pw=request.POST.get('user_pw')
            )
        })
    return JsonResponse({
        'result': False
    })
