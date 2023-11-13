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

      @action(detail=False,methods=['GET'], url_path=r'external_id/(?P<exid>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})')
      def external_id(self, request, exid):
           user = Usuario.objects.get(id_externo=str(exid))
           return Response(UsuarioSerializer.Serializer(user).data)


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
                turmas_id = map(lambda t_a:t_a['turma'], 
                                Aluno_TurmaSerializer.Serializer(Aluno_Turma.objects.filter(aluno=userSerialized['id']), 
                                                                 many=True).data)
                
                #Encontrar as turmas a partir dos ids
                turmasQuerySet = Turma.objects.filter(id__in=turmas_id)
                turmas = TurmaSerializer.Serializer(turmasQuerySet, many=True).data
                
                #Encontrar chamadas abertas a partir dos ids
                chamadas =  map(lambda chamada:chamada['turma'], ChamadaSerializer.Serializer(Chamada.objects.filter(turma__in=turmasQuerySet)
                                                        .exclude(data_inicio__gt=date)
                                                        .exclude(data_fim__lt=date)
                                                        , many=True).data)

                for turma in turmas:
                     turma['horarios'] = Turma_HorarioSerializer.Serializer(Turma_Horario.objects.filter(turma=turma['id'])
                                            , many=True).data
                     turma['aberta'] = turma['id'] in list(chamadas)
                res = {'Turmas': turmas}
            
            #Lógica para usuário do tipo Professor
            else:                
                #Encontrar as turmas que o usuário administra
                turmas = TurmaSerializer.Serializer(Turma.objects.filter(professor_id=userSerialized['id']), many=True).data
                turmas_id = map(lambda turma:turma['id'], turmas)
                dia_semana = date.weekday()

                if dia_semana < 6:
                    #Encontrar horarios a partir dos ids
                    horarios_abertos = map(lambda horario:horario['turma'],
                                Turma_HorarioSerializer.Serializer(Turma_Horario.objects.filter(turma__in=turmas_id)
                                                            .filter(dia_semana=WeekdayMap[dia_semana][0])
                                                            .exclude(hora_inicio__gt=date.hour)
                                                            .exclude(hora_fim__lt=date.hour)
                                                            , many=True).data)
                    for turma in turmas:
                        turma.aberta = turma['id'] in horarios_abertos

                horarios = map(lambda horario:horario['turma'],
                Turma_HorarioSerializer.Serializer(Turma_Horario.objects.filter(turma__in=turmas_id)
                                            , many=True).data)
                for turma in turmas:
                        turma['horarios'] = Turma_HorarioSerializer.Serializer(Turma_Horario.objects.filter(turma=turma['id'])
                                            , many=True).data

                res = {'Turmas': turmas}
                 

            return Response(res)