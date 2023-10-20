from django.test import TestCase

from .factories import *


class UsuarioTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        usuario = UsuarioFactory()
        self.assertEqual('A', usuario.usuario_tipo)

class TurmaTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        usuario = UsuarioFactory()
        turma = TurmaFactory()
        self.assertEqual(1, turma.professor_id)
