from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, UpdateView

from clients.models import Client
from .filters import MessageFilter
from .forms import MessageCreateForm, MessageUpdateForm
from .models import Message
from projects.models import Project


class CompanyMessageView(View):
    """Отображение всех сообщений компании"""
    def get(self, request, pk):

        object = get_object_or_404(Client, pk=pk)
        """Client: Передается для отображения карточки"""

        qs = Message.objects.filter(project__company__pk=pk).order_by('date')
        _filter = MessageFilter(self.request.GET, queryset=qs)

        """
        ref передается для настройки шаблона
        под тип отображения company/project
        """
        return render(request, 'communications/messageList.html',
                      context={'object': object, 'object_list': _filter.qs, 'filter': _filter, 'ref': 'company' })


class ProjectMessageView(View):
    """Отображение всех сообщений проекта"""
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        qs = project.message_set.all().order_by('date')
        _filter = MessageFilter(self.request.GET, queryset=qs)

        """
        ref передается для настройки шаблона
        под тип отображения company/project
        """
        return render(request, 'communications/messageList.html',
                      context={'object': project.company, 'project': project, 'object_list': _filter.qs, 'filter': _filter, 'ref': 'project' })


class MessageDetailView(DetailView):
    """Детальная информация о сообщении"""
    model = Message
    template_name = 'communications/messageDetail.html'


class MessageUpdateView(UpdateView):
    """Редактирование сообщения"""
    model = Message
    template_name = 'communications/messageForm.html'
    form_class = MessageUpdateForm

    def post(self, request, *args, **kwargs):
        """Присваивание имени менеджера сообщению"""
        message: Message = self.get_object()
        # TODO PRINT MANAGER NAME HERE
        message.manager = "WILL HERE SOON"
        message.save()

        return super().post(request, *args, **kwargs)


class MessageCreateView(View):
    """Создание сообщения"""
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = MessageCreateForm()
        """
        createMode передается для настройки шаблона
        под тип отображения create/update
        """
        return render(request, 'communications/messageForm.html',
                      context={'form': form, 'object': project, 'createMode': True})

    def post(self, request, pk):
        form = MessageCreateForm(request.POST)
        project = get_object_or_404(Project, pk=pk)
        if form.is_valid():
            """
            Создание сообщения с определением проекта
            и менеджера который работает с ним
            """
            message = Message.objects.create(type=form.cleaned_data['type'],
                                             project=project,
                                             manager='WILL BE SOON',  # TODO PRINT MANAGER NAME HERE
                                             description=form.cleaned_data['description'],
                                             rating=form.cleaned_data['rating']
                                             )
            return redirect(message.get_absolute_url())
        else:
            """
            createMode передается для настройки шаблона
            под тип отображения create/update
            """
            return render(request, 'communications/messageForm.html',
                          context={'form': form, 'object': project, 'createMode': True})
