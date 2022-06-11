from django.contrib.auth.models import User
from django.db import models
from LearningCatalog.models import Categoria
from rest_framework import fields, serializers
from LearningCatalog.models import UserModel, Estudiante


class getCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'imagen', 'categoriaPadre']
