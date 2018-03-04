from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import *
from private_pages.models import *

def about_us(request):
    return render(request,'home.html')

def announcements(request):
    data = Announcements.objects.all()
    context = {"data":data}
    return render(request,'announcements.html',context)

def announcements_post(request,post_id):
    data = get_object_or_404(Announcements,pk=post_id)
    context = {'data':data}
    return render(request,'announcement_post.html',context)

def event_gallery(request):
    return render(request,'event_gallery.html')

def volunteers(request):
    volunteers = Profile.objects.all()
    context = {"volunteers":volunteers }
    return render(request,'volunteers.html',context)

def contact_us(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact_us')
        else:
            return redirect('/contact_us/')
    else:
        form = MessageForm()
        context = {'form':form}
        return render(request,'contact_us.html',context)

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

def login2(request):
    return HttpResponseRedirect('/accounts/login')