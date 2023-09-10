from django.db import models


class Professor(models.Model):
    professorNome = models.CharField(max_length=60)