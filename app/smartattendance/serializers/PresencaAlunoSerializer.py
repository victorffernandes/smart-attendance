from rest_framework.serializers import ModelSerializer

from ..models import Presenca
from . import UsuarioSerializer

class Serializer(ModelSerializer):
    aluno = UsuarioSerializer.Serializer()

    class Meta:
        model = Presenca
        fields = '__all__'