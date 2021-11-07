from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Account(AbstractUser):
    """
    Расширеная версия User-а
    boolean: is_manager является ли пользователь менеджером
    image: photo фото аккаунта пользователя
    """
    is_manager = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='accounts', null=True, blank=True)

    def has_manager_perms(self):
        return self.is_superuser or self.is_manager