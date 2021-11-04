from django.urls import path

from projects.views import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectCreateView

urlpatterns = [
    path('<int:company>', ProjectListView.as_view(), name='view'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('create/<int:pk>', ProjectCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ProjectUpdateView.as_view(), name='edit'),
]
