# tests/factories.py
from factory import django, Faker

from ..models import *

#Arquivo de factories para testes unitários
#Autor: Mauricio
#Data: 12/10

class UsuarioFactory(django.DjangoModelFactory):
    usuario_nome = Faker('name')
    usuario_tipo = 'A'
    id_externo = '9dkad6c7-s649-9623-99e2-5a0dbgf5dfdz'#Faker('9dkad6c7-s649-9623-99e2-5a0dbgf5dfdz')

    class Meta:
        model = Usuario
class TurmaFactory(django.DjangoModelFactory):

    class Meta:
        model = Turma

class Aluno_TurmaFactory(django.DjangoModelFactory):

    class Meta:
        model = Aluno_Turma

class ChamadaFactory(django.DjangoModelFactory):
    
    class Meta:
        model = Chamada

class PresencaFactory(django.DjangoModelFactory):

    class Meta:
        model = Presenca

class Turma_HorarioFactory(django.DjangoModelFactory):

    class Meta:
        model = Turma_Horario