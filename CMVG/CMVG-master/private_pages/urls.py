from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'private'

urlpatterns = [
    path('announcements/',views.cmvg_announcements,name="cmvg_announcements"),
    path('announcements/create/',views.cmvg_announcements_create,name="cmvg_announcements_create"),
    path('tasks/',views.cmvg_tasks,name="cmvg_tasks"),
    path('calendar/',views.cmvg_calendar,name="cmvg_calendar"),
    path('cloud_storage/',views.cmvg_cloud_storage,name="cmvg_cloud_storage"),
    path('cloud_storage/create/',views.cmvg_cloud_storage_create,name="cmvg_cloud_storage_create"),
    path('members_directory/',views.cmvg_members_directory,name="cmvg_members_directory"),
    path('profile/',views.cmvg_profile,name="cmvg_profile")
 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
