from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    #path('new/', views.project_new, name='project_new'),
    #path('<int:pk>/', views.project_detail, name='project_detail'),
    #path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    #path('<int:pk>/delete/', views.project_delete, name='project_delete'),
]