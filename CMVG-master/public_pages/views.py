from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import RegistrationForm

def about_us(request):
    return HttpResponse("About Us Page")

def announcements(request):
    return HttpResponse("Announcement Page")

def event_gallery(request):
    return HttpResponse("Event Gallery Page")

def volunteers(request):
    return HttpResponse("Volunteers Page")

def contact_us(request):
    return HttpResponse("Contact Us Page")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user  = User.objects.create_user(username=username,password=password,email=email)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request,'registration/register.html',context)