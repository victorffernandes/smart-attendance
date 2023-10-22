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
        turma = TurmaFactory(professor_id=usuario)
        serializer = TurmaSerializer.Serializer(turma)
        self.assertEqual(getattr(usuario, 'id'), serializer.data['professor_id'])
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
        turma = TurmaFactory(professor_id=professor)
        aluno_turma = Aluno_TurmaFactory(aluno_id=aluno, turma_id=turma)
        serializer = Aluno_TurmaSerializer.Serializer(aluno_turma)
        self.assertEqual(getattr(aluno, 'id'), serializer.data['aluno_id'])
        self.assertEqual(getattr(turma, 'id'), serializer.data['turma_id'])

class Turma_HorarioSerializerTestCase(TestCase):
    def test_campos(self):
        """Comparando dados do serializer com os dados do model Turma_Horario"""
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)
        turma_horario = Turma_HorarioFactory(turma_id=turma)
        serializer = Turma_HorarioSerializer.Serializer(turma_horario)
        self.assertEqual(getattr(turma, 'id'), serializer.data['turma_id'])
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
        turma = TurmaFactory(professor_id=professor)
        chamada = ChamadaFactory(turma_id=turma)
        serializer = ChamadaSerializer.Serializer(chamada)
        self.assertEqual(getattr(turma, 'id'), serializer.data['turma_id'])
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
        turma = TurmaFactory(professor_id=professor)
        chamada = ChamadaFactory(turma_id=turma)
        aluno = UsuarioFactory()
        presenca = Presenca(aluno_id=aluno, chamada_id=chamada)
        serializer = PresencaSerializer.Serializer(presenca)
        self.assertEqual(getattr(chamada, 'id'), serializer.data['chamada_id'])
        self.assertEqual(getattr(aluno, 'id'), serializer.data['aluno_id'])
        for field_name in [
            'tempo_entrada', 'tempo_saida'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(presenca, field_name)
            )
