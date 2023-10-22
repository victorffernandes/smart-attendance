from rest_framework.serializers import ModelSerializer

from ..models import Usuario

class Serializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id', 'usuario_nome', 'usuario_tipo', 'id_externo'
        )