from django.test import TestCase

from .factories import *
from ..lib import WeekdayMap
from django.utils import timezone
import pytz
class UsuarioTestCase(TestCase):
    def test_str(self):
        #"""Teste criando usuário e associando a um tipo específico"""
        usuario = UsuarioFactory(usuario_tipo='P')
        self.assertEqual('P', usuario.usuario_tipo)

class TurmaTestCase(TestCase):
    def test_str(self):
        #"""Teste criando uma turma com um professor"""
        usuario = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=usuario)
        self.assertEqual(usuario, turma.professor)

class Aluno_TurmaTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando um aluno a uma turma"""
        professor = UsuarioFactory(usuario_tipo='P')
        aluno = UsuarioFactory()
        turma = TurmaFactory(professor=professor)
        aluno_turma = Aluno_TurmaFactory(aluno=aluno, turma=turma)
        self.assertEqual(aluno, aluno_turma.aluno)
        self.assertEqual(turma, aluno_turma.turma)

class Turma_HorarioTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando Turma_Horario a uma turma"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        turma_horario = Turma_HorarioFactory(turma=turma, dia_semana=WeekdayMap[2][0])
        self.assertEqual(turma, turma_horario.turma)
        self.assertEqual("Qua", turma_horario.dia_semana)

class ChamadaTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando uma Chamada à turma"""        
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        data = datetime.now().strftime('%Y-%m-%d-%H')
        chamada = ChamadaFactory(turma=turma, data_inicio=data)
        self.assertEqual(turma, chamada.turma)
        self.assertEqual(data, chamada.data_inicio)

class PresencaTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando uma presença a uma chamada"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        chamada = ChamadaFactory(turma=turma)
        aluno = UsuarioFactory()
        presenca = Presenca(aluno=aluno, chamada=chamada)
        self.assertEqual(aluno, presenca.aluno)
        self.assertEqual(chamada, presenca.chamada)