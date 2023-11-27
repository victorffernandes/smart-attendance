from django.db import models
from .lib import WeekdayMap

# Id externo extraído do firebase para login com o google, pelo que encontrei o id segue o formato: 9dkad6c7-s649-9623-99e2-5a0dbgf5dfdz,
# com 36 caracteres
# Autor: Mauricio
# Data: 05/10
class Usuario(models.Model):
    TYPE = [("A", "Aluno"), ("P", "Professor")]
    usuario_nome = models.CharField(max_length=60)
    usuario_tipo = models.CharField(max_length=1,choices = TYPE)
    id_externo = models.CharField(max_length=36)

class Turma(models.Model):
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    turma_nome = models.CharField(max_length=60)
    semestre = models.CharField(max_length=6)

class Aluno_Turma(models.Model):
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Chamada(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    raio = models.FloatField(null=True)

class Presenca(models.Model):
    STATUS = [("P", "Presente"), ("F","Falta"), ("C","Contestação")]
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chamada = models.ForeignKey(Chamada, on_delete=models.CASCADE)
    tempo_entrada = models.DateTimeField(null=True)
    tempo_saida = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=STATUS, default="P")
    ultima_atualizacao = models.DateTimeField(null=True)
    caminho_atestado = models.CharField(max_length=120, null=True)

class Turma_Horario(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=3,choices = WeekdayMap)
    hora_inicio = models.CharField(max_length=10)
    hora_fim = models.CharField(max_length=10)