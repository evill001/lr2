from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('info', views.rasp, name='info'),
    path('create', views.create, name='create'),
    path('news', views.news, name = 'news'),
    path('<int:pk>/delete', views.Del.as_view(), name='task-delete'),
    path('<int:pk>/update', views.Upd.as_view(), name='task-update'),
]
