from rest_framework.serializers import ModelSerializer

from ..models import Aluno_Turma

class Serializer(ModelSerializer):
    class Meta:
        model = Aluno_Turma
        fields = (
            'aluno_id', 'turma_id'
        )