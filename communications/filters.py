import django_filters
from django_filters import CharFilter
from django import forms

from .models import Message


class MessageFilter(django_filters.FilterSet):
    """
    Фильтр для сообщений по
    типу обращения
    и содержимому в описании
    """
    type = django_filters.ChoiceFilter(label='Тип обращения',
                                       choices=Message.MessageChanel.choices,
                                       field_name='type',
                                       widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
                                       )
    description = CharFilter(label='Искать в описании',
                             field_name='description',
                             lookup_expr='icontains',
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
                             )

    class Meta:
        model = Message
        fields = ['type', 'description']