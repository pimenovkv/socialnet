from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from userpage.models import UserInfo

menu = [
    {'title': 'Моя страница', 'url': '#'},
    {'title': 'Фотоальбом', 'url': '##'},
    {'title': 'Друзья', 'url': '###'}
]


def index(request, user_id:int=0):
    try:
        user_info = UserInfo.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return render(request, 'userpage/index.html', {'title': 'Моя страница', 'menu_items': menu})

    return render(request, 'userpage/index.html', {'user_info': user_info, 'menu_items': menu})
