from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log-in', views.log_in, name='log-in'),
    path('create-monster', views.create_monster, name='create-monster'),
]
