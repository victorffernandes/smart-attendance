from django.test import TestCase

from ..serializers import UsuarioSerializer
from .factories import UsuarioFactory


class UsuarioSerializerTestCase(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        usuario = UsuarioFactory()
        serializer = UsuarioSerializer.Serializer(usuario)
        for field_name in [
            'usuario_nome', 'usuario_tipo', 'id_externo'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(usuario, field_name)
            )