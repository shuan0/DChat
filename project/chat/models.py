from django.db import models
from account.models import User

class UserAvatar(models.Model):
    avatar = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
