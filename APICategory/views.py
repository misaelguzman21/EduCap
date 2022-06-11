from django.conf.urls import handler500
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import status
import logging
from LearningCatalog.models import *

# Create your views here.


class GetCategoriaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Categoria.objects.filter(categoriaPadre=None)
        serializer = getCategorySerializer(categories, many=True)
        return Response(serializer.data)


class GetSubCategoriaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        categories = Categoria.objects.filter(categoriaPadre=id)
        serializer = getCategorySerializer(categories, many=True)
        return Response(serializer.data)
