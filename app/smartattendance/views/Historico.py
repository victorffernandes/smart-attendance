from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Turma, Aluno_Turma, Chamada, Presenca
from ..serializers import TurmaSerializer

class ViewSet(GenericViewSet):
    
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

    @action(detail=True, methods=['GET'])
    def retornar_historico(self, request):
        turma_id = request.data.get('turma_id')
        turma = Turma.objects.get(id=turma_id)

        chamadas = Chamada.objects.filter(turma_id=turma.id)
        total_chamadas = chamadas.count()
        alunos = Aluno_Turma.objects.filter(turma_id=turma.id)
        total_alunos = alunos.count()
    
        presencas_aluno = []
        faltas_aluno = []
        soma_presencas = 0

        for aluno in alunos:
            presencas = Presenca.objects.filter(aluno_id=aluno.aluno_id, chamada_id__in=chamadas, status='P').count()
            faltas = Presenca.objects.filter(aluno_id=aluno.aluno_id, chamada_id__in=chamadas, status='F').count()

            if total_chamadas > 0:
                porcentagem_presenca = (presencas / total_chamadas) * 100
            else:
                porcentagem_presenca = 0

            presencas_aluno.append({
                'aluno_id': aluno.aluno_id.id,
                'presencas': presencas,
                'porcentagem_presenca': porcentagem_presenca,
            })

            faltas_aluno.append({
                'aluno_id': aluno.aluno_id.id,
                'faltas': faltas,
            })
            
        for presenca in presencas_aluno:
            soma_presencas += presenca['presencas']
        
        media_turma = soma_presencas / total_alunos

        return Response({
            'media_turma': media_turma,
            'presencas_aluno': presencas_aluno,
            'faltas_aluno': faltas_aluno,
        })