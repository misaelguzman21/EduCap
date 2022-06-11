from django.shortcuts import render
from .models import *

# Create your views here.


def Index(request):
    carrouselArray = Carrousel.objects.all()
    tarjetasArray = HomeSections.objects.all()
    jumbotronhomeArray = JumboTronHome.objects.all()

    for i in carrouselArray:
        carrousel = i

    for i in tarjetasArray:
        tarjetas = i

    for i in jumbotronhomeArray:
        jumbotronhome = i

    return render(request, "Index/index.html", {
        "carrousel": carrousel,
        "tarjetas": tarjetas,
        "jumbotron": jumbotronhome
    })
