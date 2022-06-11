from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "LearningCatalog"

urlpatterns = [
    path('Categorias', views.primaryCategory, name='primaryCategory'),
    path('Categorias/<int:pk>', views.subCategories, name='subCategories'),
    path('Busqueda/Categorias', views.searchCategory, name="searchCategory"),
    path('Lecciones', views.listLesson, name="listLesson"),
    path('Lecciones/<int:pk>', views.readLesson, name="readLesson"),
    path('Busqueda/Lecciones', views.searchLesson, name="searchLesson"),
    path('Categoria/Lecciones/<int:pk>', views.filterLessonsByCategory,
         name="filterLessonsByCategory"),
    path('Lecciones/FollowLesson',
         views.followLesson, name="followLesson"),
    path('CheckFollow/', views.checkFollow, name="checkFollow"),
        #Quizzes URL
    path('Lecciones/<int:pk>/Quiz/Nuevo', views.newQuiz, name='newQuiz'),
    path('Lecciones/<int:pk>/Quiz/<quiz_id>/NuevaPregunta', views.NewQuestion, name='NewQuestion'),
    path('Lecciones/<int:pk>/Quiz/<quiz_id>/', views.QuizDetail, name='QuizDetail'),
    path('Lecciones/<int:pk>/Quiz/<quiz_id>/Tomar', views.TakeQuiz, name='TakeQuiz'),
    path('Lecciones/<int:pk>/Quiz/<quiz_id>/Tomar/Entregar', views.SubmitQuiz, name='SubmitQuiz'),
    path('Lecciones/<int:pk>/Quiz/<quiz_id>/<attempt_id>/Resultados', views.AttemptDetail, name='AttemptDetail'),
        #Exercises URL
    path('Lecciones/<int:pk>/Exercise/Nuevo', views.newExercise, name='newExercise'),
    path('Lecciones/<int:pk>/Exercise/<exercise_id>/NuevaPregunta', views.NewQuestionExercise, name='NewQuestionExercise'),
    path('Lecciones/<int:pk>/Exercise/<exercise_id>/Tomar', views.TakeExercise, name='TakeExercise'),
    path('Lecciones/<int:pk>/Exercise/<exercise_id>/Tomar/Entregar', views.SubmitExercise, name='SubmitExercise'),
    path('Lecciones/<int:pk>/Exercise/<exercise_id>/<attempt_id>/Resultados', views.AttemptDetailExercise, name='AttemptDetailExercise'),

    path('Lecciones/<int:pk>/Encuesta', views.evaluateLesson, name='evaluateLesson'),
    path('Lecciones/Solicitar-nueva', views.solicitar, name="solicitar"),
    
    path('Lecciones/<int:pk>/Quiz/<quiz_id>/Diploma', views.Diploma, name='Diploma')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#url(r'^like/$', login_required(views.like), name='like')

