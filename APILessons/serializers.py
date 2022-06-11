from django.contrib.auth.models import User
from django.db import models
from LearningCatalog.models import Categoria
from rest_framework import fields, serializers
from LearningCatalog.models import *


class getLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = ['id', 'titulo', 'descripcion', 'imagen']


class getCategoryById(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']


class getLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = ['id', 'titulo', 'descripcion', 'imagen', 'fecha', 'category']


class getFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = ['id', 'orden', 'titulo', 'descripcion', 'path', 'lipo']


class getVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descripcion', 'link']
