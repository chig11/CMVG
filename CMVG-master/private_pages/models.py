from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=200,null=False)
    email = models.EmailField(null=False)
    image = models.ImageField(upload_to="profiles/",null=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    middle_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    nickname = models.CharField(max_length=200,null=True,blank=True)
    student_number = models.CharField(max_length=10,null=True,blank=True)
    program = models.CharField(max_length=200,null=True,blank=True)
    birthday = models.DateField(auto_now=False,null=True,blank=True)
    cm_birthday = models.DateField(auto_now=False,null=True,blank=True)
    permanent_address = models.CharField(max_length=256,null=True,blank=True)
    committee = models.CharField(max_length=50,null=True,blank=True)
    fb_account = models.CharField(max_length=200,null=True,blank=True)
    number = models.CharField(max_length=11,null=True,blank=True)
    network = models.CharField(max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CloudStorage(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    url = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(null=True,blank=True)
    created_by = models.CharField(max_length=200,null=False)
    creator_full_name = models.CharField(max_length=200,null=False)
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CloudStorage_Access(models.Model):
    article = models.ForeignKey(CloudStorage,on_delete=models.CASCADE)
    access = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Announcements(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    body = models.TextField(null=False,blank=False)
    notes = models.TextField(null=True,blank=True)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_by = models.CharField(max_length=200,null=False)
    creator_full_name = models.CharField(max_length=200,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Announcement_Images(models.Model):
    article = models.ForeignKey(Announcements,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="announcements/",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Announcement_Access(models.Model):
    article = models.ForeignKey(Announcements,on_delete=models.CASCADE)
    access = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Galleries(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_by = models.CharField(max_length=200,null=False)
    creator_full_name = models.CharField(max_length=200,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gallery_Images(models.Model):
    gallery = models.ForeignKey(Galleries,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery/",null=True)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gallery_Access(models.Model):
    gallery = models.ForeignKey(Galleries,on_delete=models.CASCADE)
    access = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)