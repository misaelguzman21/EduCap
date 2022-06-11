from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "APILessons"

urlpatterns = [
    path('lessons/getAll', views.GetLessonsView.as_view()),
    path('lesson/<int:id>', views.GetLessonView.as_view()),
    path('getCategoryById/<int:id>', views.GetCategoryByName.as_view()),
    path('getFiles/<int:id>', views.GetFilesView.as_view()),
    path('getVideos/<int:id>', views.GetVideosView.as_view()),
    path('getUserLessons', views.GetUserLessons.as_view()),
    path('getLessonsByFilter/<int:id>', views.GetLessonsByFilter.as_view()),
    path('followedLesson/<int:id>', views.GetFollowedLesson.as_view()),
    path('setFollowedLesson', views.SetFollowedLesson.as_view()),
]
