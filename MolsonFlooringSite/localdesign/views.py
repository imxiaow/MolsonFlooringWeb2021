from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

import urllib
import json

from django.urls import reverse


# Create your views here.

def homePage(request):
    context ={}
    return render(request, "localdesign/homepage.html", context)


def aboutUs(request):
    context = {}
    return render(request, "localdesign/aboutus.html", context)


def productPage(request):
    context = {}
    return render(request, "localdesign/productpage.html", context)


def servicesPage(request):
    context = {}
    return render(request, "localdesign/servicespage.html", context)


def galleryPage(request):
    context = {}
    return render(request, "localdesign/gallerypage.html", context)


def contactUs(request):
    context = {}
    return render(request, "localdesign/contactus.html", context)
