from django.urls import path

from clients.views import ClientDetailView, ClientUpdateView, ClientCreateView

urlpatterns = [
    path('<int:pk>', ClientDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name='edit'),
    path('create/', ClientCreateView.as_view(), name='create')
]
