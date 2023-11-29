from django.test import TestCase
from rest_framework import status
from datetime import datetime
from .factories import *
from ..lib import WeekdayMap
#MUDAR NOME DAS CLASES ou juntar

class IntegrationTestCase(TestCase):
    def test_associar_aluno_a_turma_e_presenca(self):
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        aluno = UsuarioFactory(usuario_tipo = 'A',id = 1)
        Aluno_TurmaFactory(aluno=aluno, turma=turma)
        response = self.client.get(f"/usuario/{aluno.id}/listar_turma/")

        self.assertEqual(response.json()["Turmas"][0]['aberta'], False)



    def test_test_associar_alunos_a_turma_e_iniciar_chamada(self):
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        aluno = UsuarioFactory(usuario_tipo = 'A',id = 1)
        Aluno_TurmaFactory(aluno=aluno, turma=turma)
        data = {
            'turma': turma.id,
            'latitude': 123.456,  
            'longitude': -78.910, 
            'data_início' : (datetime.now() - timedelta(hours=2)).strftime('%Y-%m-%d-%H'),
            'data_fim' : '240',
            'raio': 5.0,
            'latLong': 'LatLng(lat: -22.88, lng: -14.17)',
        }

        self.client.put(f'/turma/iniciar_chamada/', data, format='json', content_type='application/json')
        response1 = self.client.get(f"/usuario/{aluno.id}/listar_turma/")
        self.assertEqual(response1.json()["Turmas"][0]['aberta'], True)


class TurmaAlunoIntegrationTestCase(TestCase):
    def test_associar_alunos_a_turma(self):
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)

        aluno2 = UsuarioFactory(usuario_tipo = 'A',id = 1)
        aluno1 = UsuarioFactory(usuario_tipo = 'A', id = 2)

        Aluno_TurmaFactory(aluno=aluno1, turma=turma)
        Aluno_TurmaFactory(aluno=aluno2, turma=turma)
        response1 = self.client.get(f"/usuario/{aluno1.id}/listar_turma/")
        
        response2 = self.client.get(f"/usuario/{aluno2.id}/listar_turma/")
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

class ChamadaPresencaIntegrationTestCase(TestCase):
    def test_associar_presencas_a_chamada(self):
        usuario = UsuarioFactory(usuario_tipo = 'A')
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)
        aluno_turma = Aluno_TurmaFactory(aluno=usuario, turma=turma)
        chamada = ChamadaFactory(turma=turma)
        presenca = PresencaFactory(status="P", aluno= usuario, chamada = chamada)
        self.assertEqual(presenca.status, "P")

class UsuarioTurmaIntegrationTestCase(TestCase):
    def test_associar_turma_a_usuario(self):
        usuario = UsuarioFactory(usuario_tipo = 'A')
        professor = UsuarioFactory(usuario_tipo='P')
        turma = TurmaFactory(professor=professor)

        aluno_turma = Aluno_TurmaFactory(aluno=usuario, turma=turma)
        self.assertEqual(aluno_turma.aluno, usuario)
 
