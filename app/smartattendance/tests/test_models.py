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
        turma = TurmaFactory(professor_id=usuario)
        self.assertEqual(usuario, turma.professor_id)

class Aluno_TurmaTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando um aluno a uma turma"""
        professor = UsuarioFactory(usuario_tipo='P')
        aluno = UsuarioFactory()
        turma = TurmaFactory(professor_id=professor)
        aluno_turma = Aluno_TurmaFactory(aluno_id=aluno, turma_id=turma)
        self.assertEqual(aluno, aluno_turma.aluno_id)
        self.assertEqual(turma, aluno_turma.turma_id)

class Turma_HorarioTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando Turma_Horario a uma turma"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)
        turma_horario = Turma_HorarioFactory(turma_id=turma, dia_semana=WeekdayMap[2][0])
        self.assertEqual(turma, turma_horario.turma_id)
        self.assertEqual("Qua", turma_horario.dia_semana)

class ChamadaTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando uma Chamada à turma"""        
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)
        data = datetime.now().strftime('%Y-%m-%d-%H')
        chamada = ChamadaFactory(turma_id=turma, data_inicio=data)
        self.assertEqual(turma, chamada.turma_id)
        self.assertEqual(data, chamada.data_inicio)

class PresencaTestCase(TestCase):
    def test_str(self):
        #"""Teste, associando uma presença a uma chamada"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)
        chamada = ChamadaFactory(turma_id=turma)
        aluno = UsuarioFactory()
        presenca = Presenca(aluno_id=aluno, chamada_id=chamada)
        self.assertEqual(aluno, presenca.aluno_id)
        self.assertEqual(chamada, presenca.chamada_id)