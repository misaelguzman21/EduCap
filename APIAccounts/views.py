from django.conf.urls import handler500
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import status
import logging

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=handler500)


class RegisterStudentView(APIView):
    def post(self, request):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logging.error(serializer.errors)
        return Response(serializer.errors, status=handler500)


class GetStudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student = Estudiante.objects.get(user=request.user)
        serializer = getStudentSerializer(student)
        return Response(serializer.data)


class GetuserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = getUserSerializer(request.user)
        return Response(serializer.data)
