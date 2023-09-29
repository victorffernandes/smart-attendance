from django.db import models


class Usuario(models.Model):
    TYPE = [("A", "Aluno"), ("P", "Professor")]
    usuario_nome = models.CharField(max_length=60)
    usuario_tipo = models.CharField(max_length=1,choices = TYPE)


class Turma(models.Model):
    professor_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    turma_nome = models.CharField(max_length=60)
    semestre = models.CharField(max_length=6)

class Aluno_Turma(models.Model):
    aluno_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    turma_id = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Chamada(models.Model):
    turma_id = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateTimeField()
    eixo_x = models.FloatField()
    eixo_y = models.FloatField()

class Presenca(models.Model):
    aluno_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chamada_id = models.ForeignKey(Chamada, on_delete=models.CASCADE)
    tempo_entrada = models.DateTimeField()
    tempo_saida = models.DateTimeField()
