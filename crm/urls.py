"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from clients.views import ClientListView
from crm import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ClientListView.as_view(), name='home'),
    path('clients/', include(('clients.urls', 'clients'))),
    path('projects/', include(('projects.urls', 'projects'))),
    path('communications/', include(('communications.urls', 'communications'))),
    path('account/', include(('accounts.urls', 'accounts'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "crm.views.bad_request_view"
handler403 = "crm.views.permission_denied_view"
handler404 = "crm.views.not_found_view"
handler500 = "crm.views.server_error_view"
