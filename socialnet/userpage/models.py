from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name='userinfo', on_delete=models.CASCADE, default=None, verbose_name='Пользователь')
    age = models.PositiveSmallIntegerField(blank=True, verbose_name='Возраст')
    photo = models.ImageField(upload_to='photos/', blank=True, verbose_name='Фото')
    about = models.TextField(blank=True, verbose_name='О себе')
    friends = models.ManyToManyField(User, related_name='friends', symmetrical=False, blank=True, verbose_name='Друзья')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'
