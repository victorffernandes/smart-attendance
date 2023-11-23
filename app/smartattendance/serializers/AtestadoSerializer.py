
from rest_framework.serializers import Serializer, FileField, IntegerField

# Serializers define the API representation.
class UploadSerializer(Serializer):
    arquivo = FileField()
    presenca_id = IntegerField()
    class Meta:
        fields = ['presenca_id','arquivo']