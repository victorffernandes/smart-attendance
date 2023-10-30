from rest_framework.serializers import ModelSerializer

from ..models import Presenca

class Serializer(ModelSerializer):
    class Meta:
        model = Presenca
        fields = (
            'aluno_id', 'chamada_id', 'tempo_entrada', 'tempo_saida', 'status', 'ultima_atualizacao'
        )