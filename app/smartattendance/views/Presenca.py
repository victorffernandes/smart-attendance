from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from ..models import Turma, Aluno_Turma, Chamada, Presenca
from ..serializers import PresencaSerializer
        

class ViewSet(GenericViewSet):
    
    serializer_class = PresencaSerializer.Serializer
    queryset = Chamada.objects.all()
    
    @action(detail=False,methods=['PATCH'])
    def editar_presenca(self, request, pk=None):
        aluno_id = request.data.get('aluno')
        chamada_id = request.data.get('chamada')
        status = request.data.get('status')
        #Pegar as informações da presenca e atualiza
        presenca = Presenca.objects.get(chamada=chamada_id, aluno=aluno_id)
        presenca.status = status
        presenca.ultima_atualizacao= datetime.now()

        if(status == 'P'):
            presenca.tempo_entrada = datetime.now()
        
        presenca.save()

        presencas_serialized = PresencaSerializer.Serializer(presenca).data

        return Response(presencas_serialized)
    
        