from django.contrib import admin
from django.urls import path
from agenda.views import Agendamento,Servico
urlpatterns = [    
    path('api/servicos/', Servico, name='servicos'),
    path('api/servicos/', Servico, name='servicos'),
    path('api/servicos/<int:pk>', Servico, name='servicos'),
    path('api/agendamentos/', Agendamento, name='servicos'),
    path('api/agendamentos/', Agendamento, name='agendar'),
    path('api/agendamentos/<int:pk>', Agendamento, name='agendar'),
]