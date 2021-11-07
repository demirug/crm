from django import forms
from clients.models import Client
import re


class ClientForm(forms.Form):
    comp_name = forms.CharField(label='Название компании',
                                error_messages={'required': 'Необходимо ввести название компании'},
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    comp_description = forms.CharField(label='Описание компании',
                                       error_messages={'required': 'Необходимо ввести описание компании'},
                                       widget=forms.TextInput())

    supervisor = forms.CharField(label='Руководитель',
                                 error_messages={'required': 'Необходимо ввести руководителя компании'},
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    address = forms.CharField(label='Адрес',
                              error_messages={'required': 'Необходимо ввести адрес компании'},
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    phones = forms.CharField(label='Номер телефона',
                             error_messages={'required': 'Необходимо ввести номер телефона'},
                             widget=forms.HiddenInput())
    emails = forms.CharField(label='Email адрес',
                             error_messages={'required': 'Необходимо ввести Email'},
                             widget=forms.HiddenInput())

    def clean_emails(self):
        """Проверка всех переданных email-ов в форме на корректность"""
        for email in self.cleaned_data.get('emails').split():
            if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
                raise forms.ValidationError("Email {} некорректный".format(email))
        return self.cleaned_data.get('emails')

    def clean_phones(self):
        """Проверка всех переданных телефонных номеров в форме на корректность"""
        for number in self.cleaned_data.get('phones').split():
            if not re.search('((\+38)?\(?\d{3}\)?[\s\.-]?(\d{7}|\d{3}[\s\.-]\d{2}[\s\.-]\d{2}|\d{3}-\d{4}))', number):
                raise forms.ValidationError("Номер телефона {} некорректный".format(number))
        return self.cleaned_data.get('phones')


class ClientModelForm(ClientForm, forms.ModelForm):

    class Meta:
        model = Client
        exclude = ['manager']
