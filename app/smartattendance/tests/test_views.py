from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .factories import UsuarioFactory


class UsuarioViewSetTestCase(TestCase):
      def setUp(self):
          self.list_url = reverse('usuario-list')

      def get_detail_url(self, usuario_id):
          return (f"/usuario/{usuario_id}/")   

      def off_test_get(self):
          """Get detailed."""
          usuario = UsuarioFactory()
          response = self.client.get(self.get_detail_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data['usuario_nome'], usuario.usuario_nome)
