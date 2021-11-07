from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class ManagerRequiredMixin(AccessMixin):
    """Проверка имеет ли пользователем права менеджера"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_manager_perms():
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)