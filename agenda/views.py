from django.shortcuts import render
from .models import Servico,Agendamento
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Agendamento,Servico
from .serializer import AgendaSerializer

@api_view(['GET', 'POST'])
def servicos(request,pk):
    if request.method == 'GET':
        servico = Servico.objects.all()
        serializer = AgendaSerializer(servico, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        Servico_obj = Servico.objects.get(pk=pk)
    except servico.DoesNotExist:
        return Response({"error": "servico não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AgendaSerializer(Servico_obj)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def agendar(request,pk):
    if request.method == 'GET':
        agenda = Agendamento.objects.all()
        serializer = AgendaSerializer(agenda, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        Agendamento_obj = Agendamento.objects.get(pk=pk)
    except agenda.DoesNotExist:
        return Response({"error": "Agendamento não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AgendaSerializer(Agendamento_obj)
    return Response(serializer.data)