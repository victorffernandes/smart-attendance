from rest_framework.mixins import (
    RetrieveModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from ..lib import WeekdayMap
from ..models import Usuario, Turma, Aluno_Turma, Chamada, Turma_Horario
from ..serializers import UsuarioSerializer, TurmaSerializer, Aluno_TurmaSerializer, ChamadaSerializer, Turma_HorarioSerializer


class ViewSet(GenericViewSet, RetrieveModelMixin):

      serializer_class = UsuarioSerializer.Serializer
      queryset = Usuario.objects.all()

      @action(detail=True,methods=['GET'])
      def listar_turma(self, request, pk=None):
            date = datetime.now()
            #Pegar as informações do usuário
            user = self.get_object()
            userSerialized = UsuarioSerializer.Serializer(user).data
            res = {}
            
            
            #Lógica para usuário do tipo Aluno
            if userSerialized['usuario_tipo'] == 'A':
                #Encontrar os ids das turmas que o usuário pertence
                turmas_id = map(lambda t_a:t_a['turma_id'], 
                                Aluno_TurmaSerializer.Serializer(Aluno_Turma.objects.filter(aluno_id=userSerialized['id']), 
                                                                 many=True).data)
                
                #Encontrar as turmas a partir dos ids
                turmas = TurmaSerializer.Serializer(Turma.objects.filter(id__in=turmas_id), many=True).data
                
                #Encontrar chamadas abertas a partir dos ids
                chamadas = map(lambda chamada:chamada['turma_id'],
                               ChamadaSerializer.Serializer(Chamada.objects.filter(turma_id__in=turmas_id)
                                                        .exclude(data_inicio__gt=date)
                                                        .exclude(data_fim__lt=date)
                                                        , many=True).data)
                
                for turma in turmas:
                     turma['aberta'] = turma['id'] in chamadas

                res = {'Turmas': turmas}
            
            #Lógica para usuário do tipo Professor
            else:                
                #Encontrar as turmas que o usuário administra
                turmas = TurmaSerializer.Serializer(Turma.objects.filter(professor_id=userSerialized['id']), many=True).data
                turmas_id = map(lambda turma:turma['id'], turmas)
                
                dia_semana = date.weekday()

                if dia_semana < 6:
                    #Encontrar horarios a partir dos ids
                    horarios = map(lambda horario:horario['turma_id'],
                                Turma_HorarioSerializer.Serializer(Turma_Horario.objects.filter(turma_id__in=turmas_id)
                                                            .filter(dia_semana=WeekdayMap[dia_semana][0])
                                                            .exclude(data_inicio__gt=date.hour)
                                                            .exclude(data_fim__lt=date.hour)
                                                            , many=True).data)
                    
                    for turma in turmas:
                        turma.aberta = turma.id in horarios

                res = {'Turmas': turmas}
                 

            return Response(res)