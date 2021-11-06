from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    """Модель сообщения"""

    """Содержатся различные типы обращения"""
    class MessageChanel(models.TextChoices):
        TICKET = 'TI', _('Заявка')
        EMAIL = 'EM', _('Письмо')
        WEB_SITE = 'WS', _('Сайт')
        COMP_INIT = 'CI', _('Инициатива компании')

    type = models.CharField(max_length=2, choices=MessageChanel.choices)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    manager = models.CharField(max_length=120)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('communications:detail', args=[self.pk])

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
