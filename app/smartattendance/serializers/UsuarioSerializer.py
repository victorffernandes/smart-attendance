from rest_framework.serializers import ModelSerializer

from ..models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'usuario_nome', 'usuario_tipo', 'id_externo'
        )