# tests/factories.py
from factory import django
from faker import Faker
from random import randint

from .CustomProviders import *
from ..models import *
from ..lib import *

#Arquivo de factories para testes unitários
#Autor: Mauricio
#Data: 12/10

fake = Faker('pt_BR')
fake.add_provider(semestre_provider)
fake.add_provider(turma_provider)

class UsuarioFactory(django.DjangoModelFactory):
    usuario_nome = fake.name()
    usuario_tipo = 'A'
    id_externo = '9dkad6c7-s649-9623-99e2-5a0dbgf5dfdz'

    class Meta:
        model = Usuario
class TurmaFactory(django.DjangoModelFactory):
    def __init__(self, prof = -1):
        self.professor_id = prof if prof > 0 else randint(10,50)
        self.semestre = fake.semestre()
        self.turma_nome = fake.turma_nome()

    class Meta:
        model = Turma

class Aluno_TurmaFactory(django.DjangoModelFactory):

    def __init__(self, aluno = -1, turma = -1):
        self.aluno_id = aluno if aluno > 0 else randint(10,50)
        self.turma_id = turma if turma > 0 else randint(10,50)

    class Meta:
        model = Aluno_Turma

class ChamadaFactory(django.DjangoModelFactory):

    def __init__(self, inicio, fim, turma = -1):
        self.turma_id = turma if turma > 0 else randint(10,50)
        self.data_inicio = inicio
        self.data_fim = fim
        self.latitude = 10.0
        self.longitude = 15.2
    
    class Meta:
        model = Chamada

class PresencaFactory(django.DjangoModelFactory):
    def __init__(self, inicio, fim, aluno = -1, chamada = -1):
        self.aluno_id = aluno if aluno > 0 else randint(10,50)
        self.chamada_id = chamada if chamada > 0 else randint(10,50)
        self.tempo_entrada = inicio
        self.tempo_saida = fim
    class Meta:
        model = Presenca

class Turma_HorarioFactory(django.DjangoModelFactory):

    def __init__(self, inicio, fim, turma = -1, diasemana = 0):
        self.turma_id = turma if turma > 0 else randint(10,50)
        self.dia_semana = WeekdayMap[diasemana][0]
        self.hora_inicio = inicio
        self.hora_fim = fim
    class Meta:
        model = Turma_Horario