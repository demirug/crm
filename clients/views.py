from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(ListView):
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


class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/clientDetail.html'


class ClientUpdateView(SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/clientForm.html'
    success_message = 'Данные клиента были обновлены'

    def post(self, request, *args, **kwargs):
        """Вывод ошибок формы осуществляется через messages framework"""
        form: ClientForm = self.get_form()
        for label in form.errors.as_data():
            messages.error(request, "{}".format(*form.errors[label].as_data()[0]))
        return super().post(request, *args, **kwargs)


class ClientCreateView(SuccessMessageMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/clientForm.html'
    success_message = 'Карточка клиента была успешно создана'

    def get_context_data(self, **kwargs):
        """
            Передана перменная create_mode = True
            для изменения отображения clientForm.html
            В зависимости от наличия переменной режим
            Шаблон работает для создания или редактирования
        """
        context = super().get_context_data(**kwargs)
        context['create_mode'] = True
        return context

    def post(self, request, *args, **kwargs):
        """Вывод ошибок формы осуществляется через messages framework"""
        form: ClientForm = self.get_form()
        for label in form.errors.as_data():
            messages.error(request, "{}".format(*form.errors[label].as_data()[0]))
        return super().post(request, *args, **kwargs)
