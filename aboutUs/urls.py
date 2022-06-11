from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "aboutUs"

urlpatterns = [
    path('', views.AboutUs, name='AboutUs'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)