from rest_framework import serializers
from .models import Servico,Agendamento
class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['nome','duracao','preco']

        class Meta:
            model = Agendamento
            fields = ['servico','data_hora','cliente_nome','cliente_email']