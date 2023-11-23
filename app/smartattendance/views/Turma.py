from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from ..models import Turma, Aluno_Turma, Chamada, Presenca
from ..serializers import ChamadaSerializer
        

class ViewSet(GenericViewSet):
    
    serializer_class = ChamadaSerializer.Serializer
    queryset = Chamada.objects.all()
    
    @action(detail=False,methods=['PUT'])
    def iniciar_chamada(self, request):
        turma = request.data.get('turma')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        data_fim = request.data.get('data_fim')
        raio = request.data.get('raio')

        
        turma = Turma.objects.get(id=turma)
        # Cria uma nova chamada
        chamada = Chamada.objects.create(
            turma=turma,
            data_inicio=datetime.now(),
            data_fim=data_fim,
            latitude=latitude,
            longitude=longitude,
            raio=raio
        )
        
        chamada_serializer = ChamadaSerializer.Serializer(chamada).data
        # Filtra os alunos da turma
        alunos = Aluno_Turma.objects.filter(turma=turma)
        
        # Atualizar status de todos os alunos para "FALTA"
        for al in alunos:
            Presenca.objects.create(
                aluno = al.aluno,
                chamada = chamada,
                tempo_entrada = None,
                tempo_saida = None,
                status = "F",
                ultima_atualizacao = None,
            )

        return Response(chamada_serializer)
        