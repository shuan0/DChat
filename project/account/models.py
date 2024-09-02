from django.db import models
from django.contrib.auth.models import AbstractUser
from project.settings import STATIC_URL, MEDIA_URL

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_avatar(self):
        if self.avatar:
            return f'{MEDIA_URL}{self.avatar}'
        return f'/{STATIC_URL}account/img/user_default.png'
