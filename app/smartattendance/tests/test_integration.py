from django.test import TestCase
from rest_framework import status
from datetime import datetime
from .factories import *
from ..lib import WeekdayMap
#MUDAR NOME DAS CLASES ou juntar

class IntegrationTestCase(TestCase):
    def test_associar_aluno_a_turma_e_presenca(self):
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)
        aluno = UsuarioFactory(usuario_tipo = 'A',id = 1)
        Aluno_TurmaFactory(aluno_id=aluno, turma_id=turma)
        response = self.client.get(f"/usuario/{aluno.id}/listar_turma/")

        self.assertEqual(response.json()["Turmas"][0]['aberta'], False)



    def test_test_associar_alunos_a_turma_e_iniciar_chamada(self):
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)
        aluno = UsuarioFactory(usuario_tipo = 'A',id = 1)
        Aluno_TurmaFactory(aluno_id=aluno, turma_id=turma)
        data = {
            'turma_id': turma.id,
            'latitude': 123.456,  
            'longitude': -78.910, 
            'data_início' : (datetime.now() - timedelta(hours=2)).strftime('%Y-%m-%d-%H'),
            'data_fim' : (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%d-%H'),
            'raio': 5.0,  
        }

        self.client.put(f'/turma/iniciar_chamada/', data, format='json', content_type='application/json')
        response1 = self.client.get(f"/usuario/{aluno.id}/listar_turma/")
        self.assertEqual(response1.json()["Turmas"][0]['aberta'], True)


class TurmaAlunoIntegrationTestCase(TestCase):
    def test_associar_alunos_a_turma(self):
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)

        aluno2 = UsuarioFactory(usuario_tipo = 'A',id = 1)
        aluno1 = UsuarioFactory(usuario_tipo = 'A', id = 2)

        Aluno_TurmaFactory(aluno_id=aluno1, turma_id=turma)
        Aluno_TurmaFactory(aluno_id=aluno2, turma_id=turma)
        response1 = self.client.get(f"/usuario/{aluno1.id}/listar_turma/")
        
        response2 = self.client.get(f"/usuario/{aluno2.id}/listar_turma/")
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

class ChamadaPresencaIntegrationTestCase(TestCase):
    def test_associar_presencas_a_chamada(self):
        usuario = UsuarioFactory(usuario_tipo = 'A')
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)
        aluno_turma = Aluno_TurmaFactory(aluno_id=usuario, turma_id=turma)
        chamada = ChamadaFactory(turma_id=turma)
        presenca = PresencaFactory(status="P", aluno_id= usuario, chamada_id = chamada)
        self.assertEqual(presenca.status, "P")

class UsuarioTurmaIntegrationTestCase(TestCase):
    def test_associar_turma_a_usuario(self):
        usuario = UsuarioFactory(usuario_tipo = 'A')
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor_id=professor)

        aluno_turma = Aluno_TurmaFactory(aluno_id=usuario, turma_id=turma)
        self.assertEqual(aluno_turma.aluno_id, usuario)
 
