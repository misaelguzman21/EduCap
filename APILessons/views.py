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


class GetLessonsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lessons = Leccion.objects.all()
        serializer = getLessonsSerializer(lessons, many=True)
        return Response(serializer.data)


class GetLessonView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        lesson = Leccion.objects.get(id=id)
        serializer = getLessonSerializer(lesson)
        return Response(serializer.data)


class GetCategoryByName(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        category = Categoria.objects.get(id=id)
        serializer = getCategoryById(category)
        return Response(serializer.data)


class GetFilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        files = Archivo.objects.filter(leccion=id)
        serializer = getFilesSerializer(files, many=True)
        return Response(serializer.data)


class GetVideosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        videos = Video.objects.filter(leccion=id)
        serializer = getVideosSerializer(videos, many=True)
        return Response(serializer.data)


class GetUserLessons(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        estudiante = Estudiante.objects.get(user=request.user)
        leccion_estudiante = Estudiante_Leccione.objects.filter(
            estudiante=estudiante)
        lessons = []
        for object in leccion_estudiante:
            lessons.append(object.leccion)
        serializer = getLessonsSerializer(lessons, many=True)
        return Response(serializer.data)


class GetLessonsByFilter(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        lessons = Leccion.objects.filter(category=id)
        serializer = getLessonsSerializer(lessons, many=True)
        return Response(serializer.data)


class GetFollowedLesson(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        follow = None
        student = Estudiante.objects.get(user=request.user)
        leccion = Leccion.objects.get(id=id)
        if Estudiante_Leccione.objects.filter(estudiante=student, leccion=leccion).exists():
            follow = True
        else:
            follow = False
        return Response(follow)


class SetFollowedLesson(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        id = request.data["id"]
        follow = request.data["follow"]
        logging.error(follow)

        if (follow == "true"):
            # dejar de seguir
            estudiante = Estudiante.objects.get(user=request.user)
            leccion = Leccion.objects.get(id=id)
            estudiante_leccion = Estudiante_Leccione.objects.get(
                estudiante=estudiante,
                leccion=leccion
            )
            estudiante_leccion.delete()
            return Response(False, status=status.HTTP_201_CREATED)
        else:
            # seguir
            estudiante = Estudiante.objects.get(user=request.user)
            leccion = Leccion.objects.get(id=id)
            estudiante_leccion = Estudiante_Leccione(
                estudiante=estudiante,
                leccion=leccion
            )
            estudiante_leccion.save()
            return Response(True, status=status.HTTP_201_CREATED)
