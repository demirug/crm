from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseRedirect


class ManagerRequiredMixin(AccessMixin):
    """Проверка имеет ли пользователем права менеджера"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_manager_perms():
            return HttpResponseRedirect('/')
        return super().dispatch(request, *args, **kwargs)