from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .factories import UsuarioFactory


class UsuarioViewSetTestCase(TestCase):
      def setUp(self):
          self.list_url = reverse('usuario-list')

      def get_detail_url(self, usuario_id):
          return (f"/usuario/{usuario_id}/")   

      def test_get_list(self):
          """GET the list page of Companies."""
          usuarios = [UsuarioFactory() for i in range(0, 3)]

          response = self.client.get(self.list_url)
          print(self.list_url)
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(
              set(usuario['usuario_nome'] for usuario in response.data),
              set(usuario.usuario_nome for usuario in usuarios)
          )

      def test_get(self):
          """Get detailed."""
          usuario = UsuarioFactory()
          response = self.client.get(self.get_detail_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data['usuario_nome'], usuario.usuario_nome)

      def test_delete(self):
          """DELETEing is not implemented."""
          usuario = UsuarioFactory()
          response = self.client.delete(self.get_detail_url(usuario.id))
          self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)