from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView

from clients.models import Client
from projects.forms import ProjectUpdateForm, ProjectCreateForm
from projects.models import Project

from django.utils.timezone import now


class ProjectListView(ListView):
    """Просмотр всех проектов по выбраной компании"""
    model = Project
    template_name = 'projects/projectList.html'
    paginate_by = 3
    ordering = ['finish_date', '-start_date']

    def get_queryset(self):
        """
        Переопределение get_queryset с выборкой по id компании и
        сортировкой от активных заказов до выполненых
        """
        return Project.objects.filter(company__pk=self.kwargs['company']).order_by(*self.ordering)

    def get_context_data(self, *args, **kwargs):
        """Необходим обьект Client для отоброжение карточки"""
        context = super().get_context_data(*args, **kwargs)
        context['object'] = get_object_or_404(Client, pk=self.kwargs['company'])
        return context


class ProjectDetailView(DetailView):
    """Просмотр деталей проекта"""
    model = Project
    template_name = 'projects/projectDetail.html'


class ProjectCreateView(View):
    """Создание проекта"""
    def get(self, request, pk):
        """
        Рендеринг формы для создания проэкта
        Передается createMode для подстраивания шаблона
        между режимами create/edit
        """
        form = ProjectCreateForm()
        return render(request, 'projects/projectForm.html', {'form': form, 'pk': pk, 'createMode': True})

    def post(self, request, pk):
        """
        Создание проэкта для клиента
        с id=pk и перенаправлении на него
        pk берется из URL /projects/create/<int:pk>
        """
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            company = get_object_or_404(Client, pk=pk)
            project = Project.objects.create(company=company,
                                             name=request.POST['name'],
                                             description=request.POST['description'],
                                             price=request.POST['price']
                                             )
            return redirect(project.get_absolute_url())
        return render(request, 'projects/projectForm.html', {'form': form, 'pk': pk, 'createMode': True})


class ProjectUpdateView(UpdateView):
    """Обновление параметров проекта"""
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'projects/projectForm.html'

    def post(self, request, *args, **kwargs):
        """
        Если было изменено состояние проекта (finish/active)
        присваивается finish_date текущее время
        или присвается None в зависимости от статуса
        """
        project: Project = self.get_object()
        form: ProjectUpdateForm = self.get_form()

        if form.is_valid():
            if 'finished' in form.data:
                if not project.finished:
                    project.finish_date = now()
                    project.save()
            else:
                if project.finished:
                    project.finish_date = None
                    project.save()

        return super().post(request, *args, **kwargs)
