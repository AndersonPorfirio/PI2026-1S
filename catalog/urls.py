from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reparo/<int:pk>/', views.detalhe, name='detalhe'),
    path('sobre/', views.sobre, name='sobre'),
    path('novo/', views.novo_reparo, name='novo_reparo'),
    path('gestao/', views.painel_admin, name='painel_admin'),
    path('reparo/excluir/<int:pk>/', views.excluir_reparo, name='excluir_reparo'),
    path('usuario/excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),
    path('gestao/usuario/novo/', views.novo_usuario, name='novo_usuario'),
    path('api/v1/consultar/', views.api_reparos_list, name='api_reparos_publica'),
    path('equipamento/novo/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
]
