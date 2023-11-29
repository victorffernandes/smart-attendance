from rest_framework.serializers import ModelSerializer

from ..models import Aluno_Turma

class Serializer(ModelSerializer):
    class Meta:
        model = Aluno_Turma
        fields = '__all__'