from django import forms
from django.core.exceptions import ValidationError

from projects.models import Project


class ProjectCreateForm(forms.Form):
    """Форма для создания проекта"""

    name = forms.CharField(label="Название проекта", widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label="Описание проекта", widget=forms.Textarea(attrs={'class': "form-control"}))
    price = forms.DecimalField(label="Цена проекта", widget=forms.NumberInput(attrs={"class": "form-control"}))

    def clean_price(self):
        """Валидация стоимости проекта"""
        if self.cleaned_data['price'] <= 0:
            raise ValidationError('Цена проекта не может быть меньше 1 грн')
        return self.cleaned_data['price']


class ProjectUpdateForm(forms.ModelForm):
    """Форма для редактирование проекта"""

    name = forms.CharField(label="Название проекта", widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label="Описание проекта", widget=forms.Textarea(attrs={'class': "form-control"}))
    price = forms.DecimalField(label="Цена проекта", widget=forms.NumberInput(attrs={"class": "form-control"}))
    finished = forms.BooleanField(label="Проект завершен", initial=False, required=False, widget=forms.CheckboxInput())

    def clean_price(self):
        """Валидация стоимости проекта"""
        if self.cleaned_data['price'] <= 0:
            raise ValidationError('Цена проекта не может быть меньше 1 грн')
        return self.cleaned_data['price']

    class Meta:
        model = Project
        exclude = ['company', 'finish_date']
