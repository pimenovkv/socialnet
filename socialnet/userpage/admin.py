from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user')


admin.site.register(UserInfo, UserInfoAdmin)
