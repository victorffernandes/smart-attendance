from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from ..models import Usuario, Turma, Aluno_Turma, Chamada
from ..serializers import UsuarioSerializer, TurmaSerializer, Aluno_TurmaSerializer, ChamadaSerializer


class ViewSet(GenericViewSet, ListModelMixin):

      serializer_class = UsuarioSerializer.Serializer
      queryset = Usuario.objects.all()

      @action(detail=True,methods=['GET'])
      def listar_turma(self, request, pk=None):
            #Pegar as informações do usuário
            user = self.get_object()
            userSerialized = UsuarioSerializer.Serializer(user).data
            res = {}
            
            
            #Lógica para usuário do tipo Aluno
            if userSerialized['usuario_tipo'] == 'A':
                #Encontrar os ids das turmas que o usuário pertence
                Turmas_Aluno = Aluno_TurmaSerializer.Serializer(Aluno_Turma.objects.filter(aluno_id=userSerialized['id']), many=True).data
                turmas_id = map(lambda t_a:t_a['turma_id'], Turmas_Aluno)
                
                #Encontrar as turmas a partir dos ids
                turmas = TurmaSerializer.Serializer(Turma.objects.filter(id__in=turmas_id), many=True)
                
                #Encontrar chamadas abertas a partir dos ids
                chamadas = ChamadaSerializer.Serializer(Chamada.objects.filter(turma_id__in=turmas_id)
                                                        .exclude(data_inicio__gt=datetime.now())
                                                        .exclude(data_fim__lt=datetime.now())
                                                        , many=True)
                
                res = {'Turmas': turmas.data, 'Chamadas': chamadas.data}
            
            
            return Response(res)