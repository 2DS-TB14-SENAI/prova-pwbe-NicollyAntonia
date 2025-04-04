from django.db import models
import random

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField 
    preco = models.DecimalField(max_digits=6,decimal_places=2 )

    def __str__(self):
        return self.nome
    

class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE )
    data_hora = models.DateTimeField(('31/01/22 23:59:59.999999','%d/%m/%y %H:%M:%S.%f'))
    cliente_nome= models.CharField(max_length=100)
    cliente_email = models.EmailField(default='@gmail.com')

    def __str__(self):
        return self.servico
