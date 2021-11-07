from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView

from accounts.mixins import ManagerRequiredMixin
from clients.forms import ClientForm, ClientModelForm
from clients.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/clientList.html'
    ordering = ['pk']
    paginate_by = 10

    def get_queryset(self):
        """Переопределен get_queryset для сортировки списка по GET параметру order"""
        qs = Client.objects.all()
        available_orders = ['comp_name', '-comp_name', 'createDate', '-createDate']
        """
            Доступные поля по которым будет производится сортировка списка
            Если поле для сортировки не будет найдено в данном списке 
            Или отсуствует в GET запросе
            Сортировка происходит по значению переменной ordering
        """
        if 'order' in self.request.GET and self.request.GET.get('order') in available_orders:
            return qs.order_by(self.request.GET.get('order'))
        return qs.order_by(*self.ordering)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'clients/clientDetail.html'


class ClientUpdateView(LoginRequiredMixin, ManagerRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientModelForm
    template_name = 'clients/clientForm.html'
    success_message = 'Данные клиента были обновлены'

    def post(self, request, *args, **kwargs):
        """Вывод ошибок формы осуществляется через messages framework"""
        form: ClientForm = self.get_form()
        for label in form.errors.as_data():
            messages.error(request, "{}".format(*form.errors[label].as_data()[0]))
        return super().post(request, *args, **kwargs)


class ClientCreateView(LoginRequiredMixin, ManagerRequiredMixin, View):

    def get(self, request):
        form = ClientForm()
        return render(request, 'clients/clientForm.html', context={'form': form, 'create_mode': True})

    def post(self, request):

        form = ClientForm(request.POST)
        if form.is_valid():
            client = Client.objects.create(manager=request.user,
                                           comp_name=form.cleaned_data['comp_name'],
                                           comp_description=form.cleaned_data['comp_description'],
                                           supervisor=form.cleaned_data['supervisor'],
                                           address=form.cleaned_data['address'],
                                           phones=form.cleaned_data['phones'],
                                           emails=form.cleaned_data['emails']
                                           )

            messages.success(request, "Карточка клиента была успешно создана")
            return redirect(client.get_absolute_url())
        else:
            for label in form.errors.as_data():
                messages.error(request, "{}".format(*form.errors[label].as_data()[0]))
            return render(request, 'clients/clientForm.html', context={'form': form, 'create_mode': True})