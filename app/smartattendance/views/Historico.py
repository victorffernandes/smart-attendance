from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Turma, Aluno_Turma, Chamada, Presenca, Usuario
from ..serializers import TurmaSerializer, UsuarioSerializer

class ViewSet(GenericViewSet):
    
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

    @action(detail=True, methods=['GET'])
    def retornar_historico(self, request, pk = None):
        turma = self.get_object()

        chamadas = Chamada.objects.filter(turma=turma.id)
        total_chamadas = chamadas.count()
        alunos = Aluno_Turma.objects.filter(turma=turma.id)
        total_alunos = alunos.count()
    
        presencas_aluno = []
        faltas_aluno = []
        soma_presencas = 0

        for aluno in alunos:
            presencas = Presenca.objects.filter(aluno=aluno.aluno, chamada__in=chamadas, status='P').count()
            faltas = Presenca.objects.filter(aluno=aluno.aluno, chamada__in=chamadas, status='F').count()

            if total_chamadas > 0:
                porcentagem_presenca = (presencas / total_chamadas) * 100
            else:
                porcentagem_presenca = 0
                
            user = UsuarioSerializer.Serializer(Usuario.objects.get(id=aluno.aluno.id)).data

            presencas_aluno.append({
                'aluno_id': user['id'],
                'nome': user['usuario_nome'],
                'presencas': presencas,
                'porcentagem_presenca': porcentagem_presenca,
            })

            faltas_aluno.append({
                'aluno_id': user['id'],
                'nome': user['usuario_nome'],
                'faltas': faltas,
            })

            soma_presencas += presencas
            
        
        media_turma = soma_presencas / total_alunos

        return Response({
            'media_turma': media_turma,
            'presencas_aluno': presencas_aluno,
            'faltas_aluno': faltas_aluno,
        })