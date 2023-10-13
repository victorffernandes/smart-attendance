# views.py
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(GenericViewSet,  # generic view functionality
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = UsuarioSerializer
      queryset = Usuario.objects.all()