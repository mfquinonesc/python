from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('tasks/', views.task, name='tasks'),
    path('projects/', views.projects, name='projects'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project')
]
