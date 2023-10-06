from django.db import models

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
    professor_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    turma_nome = models.CharField(max_length=60)
    semestre = models.CharField(max_length=6)

class Aluno_Turma(models.Model):
    aluno_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    turma_id = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Chamada(models.Model):
    turma_id = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Presenca(models.Model):
    aluno_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chamada_id = models.ForeignKey(Chamada, on_delete=models.CASCADE)
    tempo_entrada = models.DateTimeField()
    tempo_saida = models.DateTimeField()

class Turma_Horario(models.Model):
    TYPE = [("Seg", "Segunda"), ("Ter", "Terça"), ("Qua", "Quarta"), ("Qui", "Quinta"), ("Sex", "Sexta"), ("Sab", "Sábado")]
    turma_id = models.ForeignKey(Turma, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=3,choices = TYPE)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()