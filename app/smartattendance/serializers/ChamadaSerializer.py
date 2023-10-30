from rest_framework.serializers import ModelSerializer

from ..models import Chamada

class Serializer(ModelSerializer):
    class Meta:
        model = Chamada
        fields = (
            'turma_id', 'data_inicio', 'data_fim', 'latitude', 'longitude', 'raio', 'caminho_atestado', 'ultima_atualizacao'
        )