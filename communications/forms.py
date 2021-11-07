from django import forms
from django.core.exceptions import ValidationError

from .models import Message


class MessageCreateForm(forms.Form):
    """Форма для создания сообщения"""
    type = forms.ChoiceField(label='Канал общения',
                             widget=forms.Select(attrs={'class': 'form-control'}),
                             choices=Message.MessageChanel.choices
                             )

    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control'})
                                  )

    rating = forms.IntegerField(label='Оценка',
                                initial=10,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10})
                                )

    def clean_rating(self):
        """
        Валидация оценки работы менеджера
        Допустимые значения от 1 до 10
        """
        rating = self.cleaned_data['rating']
        if 1 <= rating <= 10:
            return rating
        else:
            raise ValidationError('Значение оценки должно быть в лимите от 1 до 10')


class MessageUpdateForm(MessageCreateForm. forms.ModelForm):
    """
    Форма для изменения сообщения
    Наследует поля у MessageCreateForm
    """
    class Meta:
        model = Message
        exclude = ['project', 'manager']