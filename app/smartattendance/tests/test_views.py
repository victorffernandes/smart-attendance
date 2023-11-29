from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from datetime import datetime
from django.utils import timezone
import pytz
from ..lib import WeekdayMap
from .factories import *



class UsuarioViewSetTestCase(TestCase):
      def get_listar_url(self, usuario):
          return (f"/usuario/{usuario}/listar_turma/")   

      def test_get_listar_turmas_aluno_vazio(self):
          """Listar turmas aluno sem turmas inscritas"""
          usuario = UsuarioFactory()
          response = self.client.get(self.get_listar_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data['Turmas']), 0)

      def test_get_listar_turmas_usuario_inexistente(self):
          """Listar turmas, usuário não existe"""
          response = self.client.get(self.get_listar_url(1500))
          self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
      
      def test_get_listar_turmas_professor_vazio(self):
          """Listar turmas de professor sem turmas ministradas"""
          usuario = UsuarioFactory(usuario_tipo='P')
          response = self.client.get(self.get_listar_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data['Turmas']), 0)
      
      def test_get_listar_turmas_professor(self):
          """Listar turmas de professor"""
          usuario = UsuarioFactory(usuario_tipo='P')
          TurmaFactory(professor=usuario)
          TurmaFactory(professor=usuario)
          response = self.client.get(self.get_listar_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data['Turmas']), 2)
      
      def test_get_listar_turmas_professor(self):
          """Listar turmas de professor, turma com flag de horário de chamada"""
          date = datetime.now()
          dia_semana = date.weekday()
          usuario = UsuarioFactory(usuario_tipo='P')
          TurmaFactory(professor=usuario)
          turma = TurmaFactory(professor=usuario)
          Turma_HorarioFactory(turma=turma, dia_semana=WeekdayMap[dia_semana][0])
          response = self.client.get(self.get_listar_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data['Turmas']), 2)

      def test_get_listar_turmas_professor(self):
          """Listar turmas de professor, turma com flag de horário de chamada"""
          date = datetime.now()
          dia_semana = date.weekday()
          usuario = UsuarioFactory(usuario_tipo='P')
          TurmaFactory(professor=usuario)
          turma = TurmaFactory(professor=usuario)
          Turma_HorarioFactory(turma=turma, dia_semana=WeekdayMap[dia_semana][0])
          response = self.client.get(self.get_listar_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data['Turmas']), 2)

        
      def test_get_listar_turmas_aluno(self):
          """Listar turmas do aluno"""
          professor = UsuarioFactory(usuario_tipo='P')
          aluno = UsuarioFactory()
          turma1 = TurmaFactory(professor=professor)
          turma2 = TurmaFactory(professor=professor)

          Aluno_TurmaFactory(aluno=aluno, turma=turma1)
          Aluno_TurmaFactory(aluno=aluno, turma=turma2)

          response = self.client.get(self.get_listar_url(aluno.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data['Turmas']), 2)
      
      def test_get_listar_turmas_aluno(self):
          """Listar turmas do aluno, turma com flag de horário de chamada"""
          professor = UsuarioFactory(usuario_tipo='P')
          aluno = UsuarioFactory()
          turma1 = TurmaFactory(professor=professor)
          turma2 = TurmaFactory(professor=professor)

          Aluno_TurmaFactory(aluno=aluno, turma=turma1)
          Aluno_TurmaFactory(aluno=aluno, turma=turma2)
          
          ChamadaFactory(turma=turma1)

          response = self.client.get(self.get_listar_url(aluno.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(len(response.data['Turmas']), 2)
