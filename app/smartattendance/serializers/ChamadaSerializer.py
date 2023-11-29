from rest_framework.serializers import ModelSerializer

from ..models import Chamada

class Serializer(ModelSerializer):
    class Meta:
        model = Chamada
        fields = '__all__'