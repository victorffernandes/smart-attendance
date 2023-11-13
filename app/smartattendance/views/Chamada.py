from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from ..models import Turma, Aluno_Turma, Chamada, Presenca
from ..serializers import ChamadaSerializer, PresencaAlunoSerializer
        

class ViewSet(GenericViewSet):
    
    serializer_class = ChamadaSerializer.Serializer
    queryset = Chamada.objects.all()
    
    @action(detail=True,methods=['GET'])
    def lista_presenca(self, request, pk=None):
        #Pegar as informações da chamada
        chamada = self.get_object()
        chamada_serialized = ChamadaSerializer.Serializer(chamada).data
        
        presencas = Presenca.objects.prefetch_related('aluno').filter(chamada=chamada)
        presencas_serialized = PresencaAlunoSerializer.Serializer(presencas, many=True).data

        print(presencas_serialized)
        result = {'Chamada': chamada_serialized, 'Presencas': presencas_serialized}

        return Response(result)
    
        