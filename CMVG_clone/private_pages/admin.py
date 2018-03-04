from django.contrib import admin

from .models import *

admin.site.register(Profile)
admin.site.register(Announcements)
admin.site.register(CloudStorage)
admin.site.register(Galleries)
admin.site.register(Gallery_Images)
admin.site.register(Gallery_Access)
admin.site.register(Courses)