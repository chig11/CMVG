from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.admin import widgets

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
                    # 'username',
                    # 'email',
                    'image',
                    'first_name',
                    'middle_name',
                    'last_name',
                    'student_number',
                    'program',
                    'permanent_address',
                    'committee',
                    'fb_account',
                    'number',
                    'network'
                ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm,self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcements
        fields = [
                    'title',
                    'body',
                    'notes',
                    'image',
                    'created_by',
                    'creator_full_name',
                    'creator_nickname'
                ]
        widgets = {
                    'created_by':forms.HiddenInput(),
                    'creator_full_name':forms.HiddenInput(),
                    'creator_nickname':forms.HiddenInput()
                }
            
    def __init__(self,*args,**kwargs):
        super(AnnouncementForm,self).__init__(*args,**kwargs)


class CloudStorageForm(ModelForm):
    class Meta:
        model = CloudStorage
        fields = [
                    'title',
                    'url',
                    'description',
                    'created_by',
                    'creator_full_name',
                    'creator_nickname',
                    'is_pinned'
                ]
        widgets = {
                    'created_by':forms.HiddenInput(),
                    'creator_full_name':forms.HiddenInput(),
                    'creator_nickname':forms.HiddenInput(),
                    'is_pinned':forms.CheckboxInput()
                }
    
    def __init__(self,*args,**kwargs):
        super(CloudStorageForm,self).__init__(*args,**kwargs)