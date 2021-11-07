from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AccountLoginForm(forms.Form):
    """Форма для авторизации пользователя"""
    login = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AccountUpdateForm(forms.ModelForm):
    """Форма для обновления данных аккаунта"""
    first_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AccountPasswordForm(forms.Form):
    """Форма для смены пароля аккаунта"""
    old_password = forms.CharField(label='Введите старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='Введите новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password_repeat = forms.CharField(label='Повторите новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_new_password(self):
        if self.cleaned_data['new_password'] != self.cleaned_data['new_password']:
            raise ValidationError('Пароли не совпадают')

        if len(self.cleaned_data['new_password']) < 8:
            raise ValidationError('Минимальная длина пароля доожна составлять 8 символов')

        return self.cleaned_data['new_password']