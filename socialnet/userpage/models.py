from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='photos/')
    about = models.TextField(blank=True)
