from django.db import models
from django.urls import reverse


class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='photos/')
    about = models.TextField(blank=True)
    friends = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk})
