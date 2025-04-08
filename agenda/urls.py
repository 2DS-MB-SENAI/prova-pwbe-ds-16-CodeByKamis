from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.criar_ver, name='criar_ver'),
    path('api/servicos/<int:pk>', views.detalhes_servico, name='detalhes_servico'),

    path('api/servicos/', views.creat_read, name='creat_read'),
    path('api/servicos/<int:pk>', views.detalhes_agentamento, name='detalhes_agentamento'),



    # path('servicos/', views.servicos, name='servicos'),
    # path('agendamentos/', views.agendamentos, name='agendamentos'),
    # path('criar/servico/', views.criar_servico, name='criar_servico'),
    # path('detalhes/servico/', views.detalhes_servico, name='detalhes_servico'),
    # path('criar/agendamento/', views.criar_agendamento, name='criar_agendamento'),
    # path('detalhes/agendamento/', views.detalhes_agentamento, name='detalhes_agentamento'),
]

# 'consultas/<int:pk>/'