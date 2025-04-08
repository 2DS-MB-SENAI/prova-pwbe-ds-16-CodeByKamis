from django.db import models
from django.core.validators import MinLengthValidator


class Medico(models.Model):
    nome = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(5)]
    )
    escolhas_especialidade = [
        ('pediatra', 'PEDIATRA'),
        ('dentista', 'DENTISTA'),
        ('cirurgião', 'CIRURGIÃO'),
        ('car', 'CAR'),
    ]
    especialidade = models.CharField(max_length=12, choices=escolhas_especialidade)
    crm = models.CharField(max_length=8)
    email = models.EmailField()
    def __str__(self):
        return self.nome

class Consulta (models.Model):
    paciente = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status_escolhas = [
        ('AGENDADO', 'agendado'),
        ('REALIZADO', 'realizado'),
        ('CANCELADO', 'cancelado'),
    ]
    status = models.CharField(max_length=12, choices=status_escolhas)
    def __str__(self):
        return self.paciente