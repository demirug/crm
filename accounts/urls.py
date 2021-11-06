from django.urls import path

from accounts.views import *

urlpatterns = [
    path('', AccountDetailView.as_view(), name='detail'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('settings/', AccountUpdateView.as_view(), name='settings'),
    path('password/', AccountPasswordUpdateView.as_view(), name='password'),
    path('logout/', AccountLogoutView.as_view(), name='logout')
]
