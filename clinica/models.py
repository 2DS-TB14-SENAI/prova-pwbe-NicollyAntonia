from django.db import models
import random

class medico(models.Model):
    class Especialidade(models.TextChoices):
        'Cardiologia ',
        'Cases de sucesso ',
        'Gestão na saúde ',
        'Medicina Ocupacional ',
        'Médicos',
        'Neurologia' ,
        'Pacientes ',
        'Pneumologia' ,
        'Radiologia ',
        'Telemedicina' ,
        'Treinamento ',
    nome = models.CharField(max_length=100)
    crm= models.CharField(max_length=5)
    email = models.EmailField(default='@gmail.com')
    especialidade = models.CharField(max_length=20, choices=Especialidade.choices)

    def __str__(self):
        return f'{self.nome}--{self.especialidade}'
    

class consulta(models.Model):
    class agenda(models.TextChoices):
        'Agendado',
        'Realizado',
        'Cancelado'
    paciente = models.CharField(max_length=200)
    data = models.DateTimeField()
    nomemedico = models.ForeignKey(medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=200,choices=agenda.choices)


    def __str__(self):
        return f'{self.paciente}--{self.status}'