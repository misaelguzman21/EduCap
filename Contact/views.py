from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse


# Create your views here.

def Contactar(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request, "Contact/Thanks.html")
    return render(request, 'Contact/Contact.html')
