from django.test import TestCase

from ..models import Usuario
from .factories import UsuarioFactory


class UsuarioTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        usuario = UsuarioFactory()
        self.assertEqual('A', usuario.usuario_tipo)