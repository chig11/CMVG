from django.forms import ModelForm
from .models import *
from django.contrib.admin import widgets

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
                    'username',
                    'email',
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
                    'likes',
                    'shares'
                ]