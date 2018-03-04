from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.admin import widgets
# from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import *

def getTags():
    tags = [
        "Public",
        "CMVG",
        "Liturgies",
        "Creatives",
        "Ways and Means",
        "Human Resources",
        "Network and Relations"
    ]

def getCommittees():
    committees = [
            "Liturgies",
            "Creatives",
            "Ways and Means",
            "Human Resources",
            "Network and Relations"]
    return committees

def getYears(start):
    mylist = []
    while(start != 1950):
        mylist.append(str(start))
        start = start - 1
    return mylist

def getCourses():
    data = Courses.objects.all()
    return data

def cmvg_announcements(request):
    if request.user.is_authenticated:
        data = Announcements.objects.all()
        context = {"data":data}
        return render(request,'cmvg_announcements/main.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_announcement_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AnnouncementForm(request.POST,request.FILES)
            if form.is_valid():
                alpha = form.save()
                form_id = alpha.id
                return HttpResponseRedirect('/cmvg/announcements/{}/'.format(form_id))
            else: 
                return HttpResponseRedirect('/cmvg/announcements/create/')
        else:
           

            # in python manage.py shell
            # from django.contrib.auth.models import User
            # users = User.objects.all()
            # users
            #alpha = Profile.objects.get(username=request.user.username,email=request.user.email)
            # fill out /cmvg/profile fields first if you're a new user so it wouldn't return a 404 if you create a new announcement
            alpha = get_object_or_404(Profile, username=request.user.username,email=request.user.email)
            full_name = "{} {} {}".format(alpha.first_name,alpha.middle_name,alpha.last_name)           
            initial = {
                        'created_by':request.user.username,
                        'creator_full_name':full_name,
                        'creator_nickname':alpha.nickname
                      }
            form = AnnouncementForm(initial=initial)
            context = {'form':form}
            return render(request,'cmvg_announcements/create.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_announcement_edit(request,post_id=None):
    if request.user.is_authenticated:
        if request.method == "POST":
            announcement = Announcements.objects.get(pk=post_id)
            form = AnnouncementForm(request.POST,request.FILES,instance=announcement)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/cmvg/announcements/{}/'.format(post_id))
            else:
                return HttpResponseRedirect('/cmvg/announcement/edit/{}/'.format(post_id))
        else:
            alpha = get_object_or_404(Announcements,pk=post_id)
            form = AnnouncementForm(instance=alpha)
            context = {'form':form,'post_id':post_id}
            return render(request,'cmvg_announcements/edit.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_announcement_delete(request,post_id=None):
    if request.user.is_authenticated:
        announcement = Announcements.objects.get(pk=post_id)
        announcement.delete()
        return HttpResponseRedirect('/cmvg/annnouncements/')
    else:
        return HttpResponseRedirect('/')

def cmvg_announcement_post(request,post_id):
    if request.user.is_authenticated:
        data = get_object_or_404(Announcements,pk=post_id)
        context = {'data':data}
        return render(request,'cmvg_announcements/post.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_tasks(request):
    return HttpResponse("CMVG Tasks")

def cmvg_calendar(request):
    return render(request,"cmvg_calendar/index.html")

def cmvg_cloud_storage(request):
    if request.user.is_authenticated:
        data = CloudStorage.objects.all()
        context = {"data":data}
        return render(request,'cmvg_cloud_storage/main.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_cloud_storage_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CloudStorageForm(request.POST)
            if form.is_valid():
                alpha = form.save()
                form_id = alpha.id
                return HttpResponseRedirect('/cmvg/cloud_storage/{}/'.format(form_id))
            else: 
                return HttpResponseRedirect('/cmvg/cloud_storage/create/')
        else:
            alpha = Profile.objects.get(username=request.user.username,email=request.user.email)
            full_name = "{} {} {}".format(alpha.first_name,alpha.middle_name,alpha.last_name)           
            initial = {
                        'created_by':request.user.username,
                        'creator_full_name':full_name,
                        'creator_nickname':alpha.nickname
                      }
            form = CloudStorageForm(initial=initial)
            context = {'form':form}
            return render(request,'cmvg_cloud_storage/create.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_cloud_storage_edit(request,post_id=None):
    if request.user.is_authenticated:
        if request.method == "POST":
            cloudstorage = CloudStorage.objects.get(pk=post_id)
            form = CloudStorageForm(request.POST,instance=cloudstorage)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/cmvg/cloud_storage/{}/'.format(post_id))
            else:
                return HttpResponseRedirect('/cmvg/cloud_storage/edit/{}/'.format(post_id))
        else:
            alpha = get_object_or_404(CloudStorage,pk=post_id)
            form = CloudStorageForm(instance=alpha)
            context = {'form':form,'post_id':post_id}
            return render(request,'cmvg_cloud_storage/edit.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_cloud_storage_delete(request,post_id=None):
    if request.user.is_authenticated:
        cloudstorage = CloudStorage.objects.get(pk=post_id)
        cloudstorage.delete()
        return HttpResponseRedirect('/cmvg/cloud_storage/')
    else:
        return HttpResponseRedirect('/')

def cmvg_cloud_storage_post(request,post_id):
    if request.user.is_authenticated:
        data = get_object_or_404(CloudStorage,pk=post_id)
        context = {'data':data}
        return render(request,'cmvg_cloud_storage/post.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_members_directory(request):
    if request.user.is_authenticated:
        data = Profile.objects.all()
        context = {"data":data}
        return render(request,"cmvg_members_directory.html",context)
    else:
        return HttpResponseRedirect('/')

def cmvg_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            data = Profile.objects.get(user=user.id)
            data.username = user.username
            data.email = user.email
            # print(request.FILES["upload"])
            try:
                data.image = request.FILES['upload']
            except:
                pass
            data.first_name = request.POST.get('first_name')
            data.middle_name = request.POST.get('middle_name')
            data.last_name = request.POST.get('last_name')
            data.nickname = request.POST.get('nickname')
            data.student_number = request.POST.get('student_number')
            data.program = request.POST.get('program')
            data.birthday = request.POST.get('birthday')
            data.cm_birthday = request.POST.get('cm_birthday')
            data.permanent_address = request.POST.get('permanent_address')
            data.committee = request.POST.get('committee')
            data.fb_account = request.POST.get('fb_account')
            data.number = request.POST.get('number')
            data.network = request.POST.get('network')
            data.save()

            return HttpResponseRedirect('/cmvg/profile/')

        else:
            #print("dumaan tlga rito")

            user = request.user
            try:
                user_profile = Profile.objects.get(user=user.id)
            except:
                profile = Profile(user=user,username=user,email=user.email)
                profile.save()
                user_profile = Profile.objects.get(user=user.id)
            context = {
                        "user":user,
                        "user_profile":user_profile,
                        "courses":getCourses(),
                        "committees":getCommittees()
                    }
            #print(context['courses'])
            #print(user_profile.birthday)
            return render(request,'cmvg_profile/index.html',context)    
    else:
        return HttpResponseRedirect('/')

def cmvg_gallery(request):
    galleries = Galleries.objects.all().prefetch_related('gallery_images').prefetch_related("gallery_access")
    context = {"galleries":galleries}
    return render(request,'cmvg_gallery/index.html',context)

def cmvg_gallery_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get('title')
            year = request.POST.get('year')
            files = request.FILES.getlist('images')
            tags = request.POST.getlist('tags')
            if(title and files and tags):
                gallery = Galleries(title=title,year=year,created_by=request.user)
                gallery.save()
                for file in files:
                    img = Gallery_Images(gallery=gallery,image=file)
                    img.save()
                for tag in tags:
                    access = Gallery_Access(gallery=gallery,access=tag)
                    access.save()
                return HttpResponseRedirect('/cmvg/gallery/')
            else:
                return HttpResponseRedirect('/cmvg/gallery/create')
        else:
            context = {"years":getYears(2018),
                        "tags":getCommittees()}
            return render(request,'cmvg_gallery/create.html',context)
    else:
        return HttpResponseRedirect('/')

def cmvg_gallery_edit(request,post_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            gallery = Galleries.objects.get(pk=post_id)
            title = request.POST.get('title')
            year = request.POST.get('year')
            files = request.FILES.getlist('images')
            tags = request.POST.getlist('tags')
            if(gallery.title != title):
                gallery.title = title
                gallery.save()
            if(gallery.year != year):
                gallery.year = year
                gallery.save()
            return HttpResponseRedirect("/cmvg/gallery/edit/{}/".format(post_id))
        else:
            gallery = Galleries.objects.get(pk=post_id)
            context = {"gallery":gallery,
                        "years":getYears(2018),
                        "tags":getCommittees()
                        }
            return render(request,"cmvg_gallery/edit.html",context)
    else:
        return HttpResponseRedirect('/')

def cmvg_gallery_post(request,post_id):
    if request.user.is_authenticated:
        gallery = Galleries.objects.get(pk=post_id)
        context = {"gallery":gallery}
        return render(request,"cmvg_gallery/post.html",context)
    else:
        return HttpResponseRedirect('/')
    return HttpResponse("Gallery Post")

def cmvg_gallery_delete(request,post_id):
    if request.user.is_authenticated:
        gallery = Galleries.objects.get(pk=post_id)
        gallery.delete()
        return HttpResponseRedirect('/cmvg/gallery/')
    else:
        return HttpResponseRedirect('/')

def cmvg_gallery_delete_image(request,post_id,image_id):
    if request.user.is_authenticated:
        image = Gallery_Images.objects.get(pk=image_id)
        image.delete()
        return HttpResponseRedirect('/cmvg/gallery/{}/'.format(post_id))
    else:
        return HttpResponseRedirect('/')

def cmvg_gallery_delete_access(request,post_id,access_id):
    if request.user.is_authenticated:
        access = Gallery_Access.objects.get(pk=access_id)
        access.delete()
        return HttpResponseRedirect('/cmvg/gallery/{}'.format(post_id))
    else:
        return HttpResponseRedirect('/')
