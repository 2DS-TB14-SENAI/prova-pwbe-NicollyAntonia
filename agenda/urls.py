from django.contrib import admin
from django.urls import path
from agenda.views import servicos,agendar
urlpatterns = [    
    path('api/servicos/', servicos, name='servicos'),
    path('api/servicos/', servicos, name='servicos'),
    path('api/servicos/<int:pk>', servicos, name='servicos'),
    path('api/agendamentos/', agendar, name='servicos'),
    path('api/agendamentos/', agendar, name='agendar'),
    path('api/agendamentos/<int:pk>', agendar, name='agendar'),
]