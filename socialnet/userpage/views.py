from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

menu = [
    {'title': 'Моя страница', 'url': '#'},
    {'title': 'Фотоальбом', 'url': '##'},
    {'title': 'Друзья', 'url': '###'}
]


def index(request, user_id:int=0):
    try:
        user = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return render(request, 'userpage/index.html', {'title': 'Моя страница', 'menu_items': menu})

    return render(request, 'userpage/index.html', {'user': user, 'menu_items': menu})
