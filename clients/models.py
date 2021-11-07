from django.db import models
from django.urls import reverse

from accounts.models import Account


class Client(models.Model):
    manager = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    comp_name = models.CharField(max_length=160)
    comp_description = models.TextField(max_length=300)
    supervisor = models.CharField(max_length=120)

    createDate = models.DateTimeField(auto_now_add=True)
    editDate = models.DateTimeField(auto_now=True)

    address = models.CharField(max_length=120)
    phones = models.TextField()
    emails = models.TextField()

    def get_absolute_url(self):
        return reverse('clients:detail', args=[self.pk])

    def __str__(self):
        return self.comp_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
