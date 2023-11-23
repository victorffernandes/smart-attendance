from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Presenca
from ..serializers import AtestadoSerializer

class ViewSet(GenericViewSet):

    serializer_class = AtestadoSerializer

    @action(detail=False, methods=['POST'])
    def inserir(self, request):
        arquivo = request.FILES.get('arquivo')
        content_type = arquivo.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)