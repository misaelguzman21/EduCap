from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def AboutUs(request):
    aboutUsArray = SobreNosotros.objects.all()

    for i in aboutUsArray:
        about = i

    people = Persona.objects.all().order_by('nombre')

    return render(request, "aboutUs/aboutUs.html", {
        "about": about,
        "people": people
    })



