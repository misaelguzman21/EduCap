from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import urls
from LearningCatalog.models import Categoria
import logging
from .models import *
from accounts.models import *
import json
from copy import copy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .form import NewQuizForm, NewQuestionForm, NewExerciseForm, NewQuestionExerciseForm
import LearningCatalog

# Create your views here.

def newQuiz(request, pk):
    user = request.user
    lesson = Leccion.objects.get(pk=pk)

    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            title  = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            allowed_attempts = form.cleaned_data.get('allowed_attempts')
            time_limit_mins  = form.cleaned_data.get('time_limit_mins')
            quiz = Quizzes.objects.create(user=user, title=title, description=description, allowed_attempts=allowed_attempts, time_limit_mins=time_limit_mins)
            lesson.quizzes.add(quiz)
            lesson.save()
            return redirect('LearningCatalog:NewQuestion',  pk=pk, quiz_id=quiz.id)

    else:
        form = NewQuizForm()
    context = {
        'form': form,
        'pk':pk
    }
    return render(request, 'LearningCatalog/CreateQuiz.html', context)
###########################################
def Diploma(request, pk, quiz_id):
    user = request.user
    lesson = Leccion.objects.get(pk=pk)
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    return render(request, 'LearningCatalog/pdf.html')
###########################################
def NewQuestion(request, pk,  quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)

    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data.get('question_text')
            points = form.cleaned_data.get('points')
            answer_text = request.POST.getlist('answer_text')
            is_correct = request.POST.getlist('is_correct')

            question = Question.objects.create(question_text=question_text, user=user, points=points)

            for a,c in zip(answer_text, is_correct):
                answer = Answer.objects.create(answer_text=a, is_correct=c, user=user)
                question.answers.add(answer)
                question.save()
                quiz.questions.add(question)
                quiz.save()
            return redirect('LearningCatalog:NewQuestion',  pk=pk,quiz_id=quiz.id)
    
    else:
        form = NewQuestionForm()
    
    context = {
        'form': form,
    }
    return render(request, 'LearningCatalog/NewQuestion.html', context)


def QuizDetail(request, pk,  quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    my_attempts = Attempter.objects.filter(quiz = quiz, user=user)

    context = {
        'quiz': quiz,
        'my_attempts': my_attempts,
        'pk': pk
    }
    return render(request, 'LearningCatalog/QuizDetail.html', context)


def TakeQuiz(request, pk,  quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)

    context = {
        'quiz': quiz,
        'pk': pk,
    }
    return render(request, 'LearningCatalog/TakeQuiz.html', context)


def SubmitQuiz(request, pk, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    earned_points = 0
    if request.method == 'POST':
        questions = request.POST.getlist('question')
        answers = request.POST.getlist('answer')
        attempter = Attempter.objects.create(quiz=quiz, user=user, score=0)

        for q,a in zip(questions, answers):
            question = Question.objects.get(id=q)
            answer =  Answer.objects.get(id=a)
            Attempt.objects.create(quiz=quiz, attempter=attempter, question=question, answer=answer)
            if answer.is_correct == True:
                earned_points += question.points
                attempter.score += earned_points
                attempter.save()
        return redirect('LearningCatalog:listLesson')


def AttemptDetail(request, pk, quiz_id, attempt_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    attempts = Attempt.objects.filter(quiz=quiz, attempter__user=user)

    context = {
        'quiz': quiz,
        'attempts' : attempts,
        'pk': pk,

    }
    return render(request,"LearningCatalog/AttemptDetail.html", context)

def primaryCategory(request):
    # Respuesta HTTPS donde django procesa el html y presenta la ingerfaz
    return render(request, "LearningCatalog/primaryCategory.html", {
        # Contexto para procesar la interfaz donde se realiza un query a la base de datos y obtenemos todas las categorias
        "categories": Categoria.objects.all().order_by('nombre'),

    })


def subCategories(request, pk):
    category = Categoria.objects.get(pk=pk)
    subCategory = Categoria.objects.filter(categoriaPadre=category)
    logging.error(subCategory)
    return render(request, "LearningCatalog/subcategory.html", {
        "category": Categoria.objects.get(pk=pk),
        "subCategories": subCategory,
    })


def searchCategory(request):
    if request.method == "POST":
        search = request.POST.get('searchBar')
        return render(request, "LearningCatalog/searchBar.html", {
            "categories": Categoria.objects.filter(Q(nombre__icontains=search) | Q(descripcion__icontains=search)),
            "search": search
        })


def listLesson(request):
    lessons = Leccion.objects.all().order_by('titulo')
    return render(request, "LearningCatalog/lessonList.html", {
        "lessons": lessons
    })


    
def readLesson(request, pk):
    lesson = Leccion.objects.get(pk=pk)
    files = Archivo.objects.filter(leccion=pk).order_by('orden')
    videos = Video.objects.filter(leccion=pk)

    # Convertir urls de youtube a urls de Embed

    arrVidL = [video.link for video in videos]
    arrVidT = [video.titulo for video in videos]
    arrVidD = [video.descripcion for video in videos]

    videoCode = []
    vidLists = []
    for i in arrVidL:
        arrLinks = []
        arrLinks = i.split('/')

        videoCode.append(arrLinks[3])

    vidLists = list(zip(arrVidT, arrVidD, videoCode))

    ##############################################

    leccion = Leccion.objects.get(pk=pk)

    if request.user.is_anonymous:
        follow = True
    else:
        if request.user.is_staff:

            follow = False
        else:
            estudiante = Estudiante.objects.get(user=request.user)
            if Estudiante_Leccione.objects.filter(estudiante=estudiante, leccion=leccion).exists():
                follow = True
            else:
                follow = False
    return render(request, "LearningCatalog/lesson.html", {
        "lesson": lesson,
        "files": files,
        "follow": follow,
        "vidLists": vidLists,


    })


def searchLesson(request):
    if request.method == "POST":
        search = request.POST.get('searchBar')
        return render(request, "LearningCatalog/lessonList.html", {
            "lessons": Leccion.objects.filter(Q(titulo__icontains=search) | Q(descripcion__icontains=search)),
            "search": search
        })


def filterLessonsByCategory(request, pk):
    subCategory = Categoria.objects.get(pk=pk)
    lessons = Leccion.objects.filter(category=subCategory)
    return render(request, "LearningCatalog/lessonList.html", {
        "lessons": lessons
    })


def followLesson(request):
    if request.is_ajax():
        if request.method == "POST":
            jsonObject = json.load(request)['jsonBody']
            pk = jsonObject["pk"]
            estudiante = Estudiante.objects.get(user=request.user)
            leccion = Leccion.objects.get(pk=pk)
            if Estudiante_Leccione.objects.filter(estudiante=estudiante, leccion=leccion).exists():
                newUnfollow = Estudiante_Leccione.objects.get(
                    estudiante=estudiante,
                    leccion=leccion
                )
                newUnfollow.delete()
                return HttpResponse("follow")
            else:
                newFollow = Estudiante_Leccione(
                    estudiante=estudiante,
                    leccion=leccion
                )
                newFollow.save()
                return HttpResponse("unFollow")


def checkFollow(request):
    return HttpResponse()

def evaluateLesson(request, pk):
    lesson = Leccion.objects.get(pk=pk)
    if request.method == "POST":
        evaluar = Encuesta()
        title_leccion = request.POST.get('title_leccion')
        pregunta1 = request.POST.get('pregunta1')
        pregunta2 = request.POST.get('pregunta2')
        pregunta3 = request.POST.get('pregunta3')
        pregunta4 = request.POST.get('pregunta4')
        pregunta5 = request.POST.get('pregunta5')
        opinion = request.POST.get('opinion')
        evaluar.title_leccion = title_leccion
        evaluar.pregunta1 = pregunta1
        evaluar.pregunta2 = pregunta2
        evaluar.pregunta3 = pregunta3
        evaluar.pregunta4 = pregunta4
        evaluar.pregunta5 = pregunta5
        evaluar.opinion = opinion
        evaluar.save()
        return render(request, 'LearningCatalog/Thanks2.html')
    return render(request, "LearningCatalog/evaluateLessons.html", {
        "lesson": lesson
    })

def solicitar(request):
    if request.method == "POST":
        solicitar = Solicitar()
        user = request.POST.get('user')
        nombre_leccion = request.POST.get('nombre_leccion')
        contenido = request.POST.get('contenido')
        solicitar.user = user
        solicitar.nombre_leccion = nombre_leccion
        solicitar.contenido = contenido
        solicitar.save()
        return render(request, 'LearningCatalog/Thanks.html')
    return render(request, 'LearningCatalog/Request.html')

# Create your views here./////////////////////////////////////////////////////////////////

def newExercise(request, pk):
    user = request.user
    lesson = Leccion.objects.get(pk=pk)

    if request.method == 'POST':
        form = NewExerciseForm(request.POST)
        if form.is_valid():
            title  = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            exercise = Exercises.objects.create(user=user, title=title, description=description)
            lesson.exercises.add(exercise)
            lesson.save()
            return redirect('LearningCatalog:NewQuestionExercise',  pk=pk, exercise_id=exercise.id)

    else:
        form = NewExerciseForm()
    context = {
        'form': form,
        'pk':pk
    }
    return render(request, 'LearningCatalog/CreateExercise.html', context)


def NewQuestionExercise(request, pk,  exercise_id):
    user = request.user
    exercise = get_object_or_404(Exercises, id=exercise_id)

    if request.method == 'POST':
        form = NewQuestionExerciseForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data.get('question_text')
            points = form.cleaned_data.get('points')
            answer_text = request.POST.getlist('answer_text')
            is_correct = request.POST.getlist('is_correct')

            question = QuestionExercise.objects.create(question_text=question_text, user=user, points=points)

            for a,c in zip(answer_text, is_correct):
                answer = AnswerExercise.objects.create(answer_text=a, is_correct=c, user=user)
                question.answers.add(answer)
                question.save()
                exercise.questions.add(question)
                exercise.save()
            return redirect('LearningCatalog:NewQuestionExercise',  pk=pk,exercise_id=exercise.id)
    
    else:
        form = NewQuestionExerciseForm()
    
    context = {
        'form': form,
    }
    return render(request, 'LearningCatalog/NewQuestionExercise.html', context)


def TakeExercise(request, pk,  exercise_id):
    exercise = get_object_or_404(Exercises, id=exercise_id)

    context = {
        'exercise': exercise,
        'pk': pk,
    }
    return render(request, 'LearningCatalog/TakeExercise.html', context)


def SubmitExercise(request, pk, exercise_id):
    user = request.user
    exercise = get_object_or_404(Exercises, id=exercise_id)
    earned_points = 0
    if request.method == 'POST':
        questions = request.POST.getlist('question')
        answers = request.POST.getlist('answer')
        attempter = AttempterExercise.objects.create(exercise=exercise, user=user, score=0)

        for q,a in zip(questions, answers):
            question = QuestionExercise.objects.get(id=q)
            answer =  AnswerExercise.objects.get(id=a)
            AttemptExercise.objects.create(exercise=exercise, question=question, answer=answer)
            if answer.is_correct == True:
                earned_points += question.points
                attempter.score += earned_points
                attempter.save()
        return redirect('LearningCatalog:listLesson')
        


def AttemptDetailExercise(request, pk, exercise_id, attempt_id):
    user = request.user
    exercise = get_object_or_404(Exercises, id=exercise_id)
    attempts = AttemptExercise.objects.filter(exercise=exercise, attempter__user=user)

    context = {
        'exercise': exercise,
        'attempts' : attempts,
        'pk': pk,

    }
    return render(request,"LearningCatalog/AttemptDetailExercise.html", context)

def ExcerciseDetail(request, pk,  exercise_id):
    user = request.user
    exercise = get_object_or_404(Exercises, id=exercise_id)
    context = {
        'exercise': exercise,
        'pk': pk
    }
    return render(request, 'LearningCatalog/ExerciseDetail.html', context)