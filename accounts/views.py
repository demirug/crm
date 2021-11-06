from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views import View

from .forms import AccountUpdateForm, AccountPasswordForm, AccountLoginForm


class AccountLoginView(View):
    """Авторизация пользователя"""

    def get(self, request: WSGIRequest):
        if request.user.is_active:
            return redirect(request.GET.get('next') or '/')
        form = AccountLoginForm()
        return render(request, 'accounts/accountLogin.html', context={'form': form})

    def post(self, request):
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            _login = form.cleaned_data['login']
            _password = form.cleaned_data['password']
            user = authenticate(username=_login, password=_password)
            login(request, user)
            return redirect(request.GET.get('next') or '/')
        else:
            return render(request, 'accounts/accountLogin.html', context={'form': form})


class AccountLogoutView(View):
    """Выход пользователя из акаунта"""
    def get(self, request):
        logout(request)
        return redirect('/')


class AccountUpdateView(LoginRequiredMixin, View):
    """
    Обновление настроек пользователя
    Поля: фамилия, имя, email
    """
    def get(self, request):
        form = AccountUpdateForm(instance=request.user)
        return render(request, 'accounts/accountSettings.html', context={'form': form})

    def post(self, request):
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные были успешно изменены')
            return redirect('accounts:detail')
        return render(request, 'accounts/accountSettings.html', context={'form': form})


class AccountPasswordUpdateView(LoginRequiredMixin, View):
    """Обновление пароля пользователя"""
    def get(self, request):
        form = AccountPasswordForm()
        return render(request, 'accounts/accountPassword.html', context={'form': form})

    def post(self, request: WSGIRequest):
        form = AccountPasswordForm(request.POST)
        if form.is_valid():
            if check_password(form.cleaned_data['old_password'], request.user.password):
                request.user.set_password(form.cleaned_data['new_password'])
                request.user.save()
                messages.success(request, 'Пароль был успешно изменены')
                return redirect('accounts:detail')
            else:
                messages.error(request, 'Неверный старый пароль')
                return render(request, 'accounts/accountPassword.html', context={'form': form})
        return render(request, 'accounts/accountPassword.html', context={'form': form})


class AccountDetailView(LoginRequiredMixin, View):
    """Детальная информация о пользователе"""
    def get(self, request):
        return render(request, 'accounts/accountDetail.html', context={'object': request.user})