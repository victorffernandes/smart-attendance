from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from ..models import Turma, Aluno_Turma, Chamada, Presenca
from ..serializers import ChamadaSerializer
        

class IniciarChamada(GenericViewSet):
    
    serializer_class = ChamadaSerializer.Serializer
    queryset = Chamada.objects.all()
    
    @action(detail=True,methods=['PUT'])
    def iniciar_chamada(self, request, turma_id):
        turma = Turma.objects.get(id=turma_id)
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        raio = request.data.get('raio')

        # Cria uma nova chamada
        chamada = Chamada.objects.create(
            turma_id=turma,
            data_inicio=datetime.now(),
            latitude=latitude,
            longitude=longitude,
            raio=raio
        )
        
        chamada_serializer = ChamadaSerializer.Serializer(chamada).data
        chamada_id = chamada_serializer['id']

        # Filtra os alunos da turma
        alunos = Aluno_Turma.objects.filter(turma_id=turma_id)
        
        # Atualizar status de todos os alunos para "FALTA"
        for aluno in alunos:
            presenca = Presenca.objects.create(
                aluno_id = aluno.aluno_id,
                chamada_id = chamada_id,
                tempo_entrada = None,
                tempo_saida = None,
                status = "F",
                ultima_atualizacao = None,
                caminho_atestado = ""
            )

        return Response(chamada_serializer)
        