from django.shortcuts import render
from django.http import HttpResponse

menu = [
    ('Моя страница', '#'),
    ('Фотоальбом', '##'),
    ('Друзья', '###')
]


def index(request):
    return render(request, 'userpage/index.html', {'tytle': 'Моя страница', 'menu_items': menu})
