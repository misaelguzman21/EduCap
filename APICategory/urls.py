from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "APICategory"

urlpatterns = [
    path('category/getAll', views.GetCategoriaView.as_view()),
    path('category/getSub/<int:id>', views.GetSubCategoriaView.as_view()),
]
