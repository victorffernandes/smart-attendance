from rest_framework.serializers import ModelSerializer

from ..models import Turma_Horario

class Serializer(ModelSerializer):
    class Meta:
        model = Turma_Horario
        fields = (
            'turma_id', 'dia_semana', 'hora_inicio', 'hora_fim'
        )