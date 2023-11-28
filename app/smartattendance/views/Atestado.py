from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files import File
from django.http import HttpResponse
from datetime import datetime

from ..models import Presenca
from ..serializers import PresencaSerializer

class ViewSet(GenericViewSet):

    parser_classes = [MultiPartParser]
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer.Serializer

    @action(detail=False, methods=['POST'])
    def inserir(self, request, format=None):
        file_obj = request.data['atestado']
        chamada = request.data['chamada']
        aluno = request.data['aluno']

        presenca = Presenca.objects.get(chamada=chamada, aluno=aluno)
        path = 'var/lib/atestado/' + str(presenca.id) + '.jpg'
        presenca.status = 'C'
        presenca.caminho_atestado = path
        presenca.ultima_atualizacao = datetime.now()

        
        destination = open(path, 'wb+')
        for chunk in file_obj.chunks():
            destination.write(chunk)
        destination.close()

        presenca.save()



        return Response(status=204)

    @action(detail=True, methods=['GET'])
    def retornar(self, request, format=None, pk=None):
        presenca = self.get_object()
        atestado = open(presenca.caminho_atestado, 'rb')
        response = HttpResponse(File(atestado), content_type='image/jpg')
        return response