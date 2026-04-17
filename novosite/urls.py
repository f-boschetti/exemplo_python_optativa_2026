from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('salvar/', views.salvar, name='salvar'),
    path('visualizar/<int:id>/', views.visualizar, name='visualizar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('update/<int:id>/', views.update, name='update'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
]
