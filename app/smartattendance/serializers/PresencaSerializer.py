from rest_framework.serializers import ModelSerializer

from ..models import Presenca

class Serializer(ModelSerializer):
    class Meta:
        model = Presenca
        fields = '__all__'