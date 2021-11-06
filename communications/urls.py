from django.urls import path

from communications.views import *

urlpatterns = [
    path('company/<int:pk>', CompanyMessageView.as_view(), name='company'),
    path('project/<int:pk>', ProjectMessageView.as_view(), name='project'),
    path('detail/<int:pk>', MessageDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', MessageUpdateView.as_view(), name='edit'),
    path('create/<int:pk>', MessageCreateView.as_view(), name='create'),
]
