from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.admin import widgets

from .forms import *
from .models import *

def cmvg_announcements(request):
    return HttpResponse("CMVG Announcements")

def cmvg_announcements_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pass
        else:
            form = AnnouncementForm()
            context = {'form':form}
            return render(request,'cmvg_announcements_create.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_tasks(request):
    return HttpResponse("CMVG Tasks")

def cmvg_calendar(request):
    return HttpResponse("CMVG Calendar")

def cmvg_cloud_storage(request):
    return HttpResponse("CMVG Cloud Storage")

def cmvg_cloud_storage_create(request):
    return HttpResponse('Create Link for Storage')

def cmvg_members_directory(request):
    return HttpResponse("CMVG Members Directory")

def cmvg_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            alpha = Profile.objects.get(username=request.user.username,email=request.user.email)
            form = ProfileForm(request.POST,request.FILES,instance=alpha)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/cmvg/profile/')
        else:
            try:
                alpha = Profile.objects.get(username=request.user.username,email=request.user.email)
            except:
                beta = Profile(username=request.user.username,email=request.user.email)
                beta.save()
                alpha = Profile.objects.get(username=request.user.username,email=request.user.email)
            form = ProfileForm(instance=alpha)
            context = {'form':form}
            return render(request,'cmvg_profile.html',context)
            
    else:
        return HttpResponseRedirect('/')