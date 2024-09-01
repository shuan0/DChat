from django.db import models
from django.contrib.auth.models import AbstractUser
from project.settings import STATIC_URL, MEDIA_URL

class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return f'{MEDIA_URL}{self.image}'
        return f'/{STATIC_URL}account/img/user_default.png'
