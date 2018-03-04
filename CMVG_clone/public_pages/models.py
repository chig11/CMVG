from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=False,blank=False)
    message = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)