# tests/factories.py
from factory import django
from faker import Faker
from random import randint

from .CustomProviders import *
from ..models import *
from ..lib import *
from datetime import datetime, timedelta

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
    semestre = fake.semestre()
    turma_nome = fake.turma_nome()

    class Meta:
        model = Turma

class Aluno_TurmaFactory(django.DjangoModelFactory):

    class Meta:
        model = Aluno_Turma

class ChamadaFactory(django.DjangoModelFactory):
    data_inicio = datetime.now().strftime('%Y-%m-%d-%H')
    data_fim = (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%d-%H')
    latitude = 10.0
    longitude = 15.2
    
    class Meta:
        model = Chamada

class PresencaFactory(django.DjangoModelFactory):
    tempo_entrada = datetime.now().strftime('%Y-%m-%d-%H')
    tempo_saida = (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%d-%H')
    class Meta:
        model = Presenca

class Turma_HorarioFactory(django.DjangoModelFactory):
    dia_semana = WeekdayMap[0][0]
    hora_inicio = datetime.now().strftime('%H')
    hora_fim = (datetime.now() + timedelta(hours=2)).strftime('%H')
    class Meta:
        model = Turma_Horario