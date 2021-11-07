from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Модель проекта"""
    company = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    finished = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('projects:detail', args=[self.pk])

    def __str__(self):
        return self.company.comp_name + " / " + self.name

    class Meta:
        unique_together = [['company', 'name']]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
