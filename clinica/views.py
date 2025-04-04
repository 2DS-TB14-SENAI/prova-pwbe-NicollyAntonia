from django.shortcuts import render
from .models import consulta, medico
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import consultaSerializer

def listar_medicos(request):
    medicos = medico.objects.all()
    return render (request, 'listar_medico.html', {'listar_medico': listar_medico})

def criar_consulta(request):
    paciente = request.data.get('paciente')
    data = request.data.get('data')
    medico = request.data.get('medico')
    status = request.data.get('status')
    if not all ([paciente,data,medico]):
        return render ({'error':'informações insuficientes para agendar consulta'}, status=status.HTTP_400_BAD_REQUEST)


def detalhes_consulta(request,pk):
    try:
        consulta_obj = consulta.objects.get(pk=pk)
    except consulta.DoesNotExist:
        return Response({"error": "Evento não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    serializer = consultaSerializer(consulta_obj)
    return Response(request, 'form_consulta.html', {'form_consulta': form_consulta})