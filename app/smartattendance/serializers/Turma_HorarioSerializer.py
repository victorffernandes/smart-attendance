from rest_framework.serializers import ModelSerializer

from ..models import Turma_Horario

class Serializer(ModelSerializer):
    class Meta:
        model = Turma_Horario
        fields = '__all__'