from django.test import TestCase

from ..serializers import UsuarioSerializer, TurmaSerializer, Aluno_TurmaSerializer, ChamadaSerializer, Turma_HorarioSerializer, PresencaSerializer
from .factories import *


class UsuarioSerializerTestCase(TestCase):
    def test_campos(self):
        """Comparando dados do serializer com os dados do model Usuario"""
        usuario = UsuarioFactory()
        serializer = UsuarioSerializer.Serializer(usuario)
        for field_name in [
            'id','usuario_nome', 'usuario_tipo', 'id_externo'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(usuario, field_name)
            )

class TurmaSerializerTestCase(TestCase):
    def test_campos(self):
        """Comparando dados do serializer com os dados do model Turma"""
        usuario = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=usuario)
        serializer = TurmaSerializer.Serializer(turma)
        self.assertEqual(getattr(usuario, 'id'), serializer.data['professor'])
        for field_name in [
            'id', 'turma_nome', 'semestre'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(turma, field_name)
            )

class Aluno_TurmaSerializerTestCase(TestCase):
    def test_campos(self):
        """Comparando dados do serializer com os dados do model Aluno_Turma"""
        professor = UsuarioFactory(usuario_tipo='P')
        aluno = UsuarioFactory()
        turma = TurmaFactory(professor=professor)
        aluno_turma = Aluno_TurmaFactory(aluno=aluno, turma=turma)
        serializer = Aluno_TurmaSerializer.Serializer(aluno_turma)
        self.assertEqual(getattr(aluno, 'id'), serializer.data['aluno'])
        self.assertEqual(getattr(turma, 'id'), serializer.data['turma'])

class Turma_HorarioSerializerTestCase(TestCase):
    def test_campos(self):
        """Comparando dados do serializer com os dados do model Turma_Horario"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        turma_horario = Turma_HorarioFactory(turma=turma)
        serializer = Turma_HorarioSerializer.Serializer(turma_horario)
        self.assertEqual(getattr(turma, 'id'), serializer.data['turma'])
        for field_name in [
            'dia_semana', 'hora_inicio', 'hora_fim'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(turma_horario, field_name)
            )


class ChamadaSerializerTestCase(TestCase):
    def test_campos(self):
        """Comparando dados do serializer com os dados do model Chamada"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        chamada = ChamadaFactory(turma=turma)
        serializer = ChamadaSerializer.Serializer(chamada)
        self.assertEqual(getattr(turma, 'id'), serializer.data['turma'])
        for field_name in [
            'data_inicio', 'data_fim', 'latitude', 'longitude'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(chamada, field_name)
            )

class PresencaSerializerTestCase(TestCase):
    def test_campos(self):
        """Comparando dados do serializer com os dados do model Presenca"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        chamada = ChamadaFactory(turma=turma)
        aluno = UsuarioFactory()
        presenca = Presenca(aluno=aluno, chamada=chamada)
        serializer = PresencaSerializer.Serializer(presenca)
        self.assertEqual(getattr(chamada, 'id'), serializer.data['chamada'])
        self.assertEqual(getattr(aluno, 'id'), serializer.data['aluno'])
        for field_name in [
            'tempo_entrada', 'tempo_saida'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(presenca, field_name)
            )
