from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'private'

urlpatterns = [
    path('announcements/',views.cmvg_announcements,name="cmvg_announcements"),
    path('announcements/create/',views.cmvg_announcement_create,name="cmvg_announcement_create"),
    path('announcements/edit/<int:post_id>/',views.cmvg_announcement_edit,name="cmvg_announcement_edit"),
    path('announcements/delete/<int:post_id>/',views.cmvg_announcement_delete,name="cmvg_announcement_delete"),
    path('announcements/<int:post_id>/',views.cmvg_announcement_post,name="cmvg_announcement_post"),
    
    path('tasks/',views.cmvg_tasks,name="cmvg_tasks"),
    
    path('calendar/',views.cmvg_calendar,name="cmvg_calendar"),
    
    path('cloud_storage/',views.cmvg_cloud_storage,name="cmvg_cloud_storage"),
    path('cloud_storage/create/',views.cmvg_cloud_storage_create,name="cmvg_cloud_storage_create"),
    path('cloud_storage/edit/<int:post_id>/',views.cmvg_cloud_storage_edit,name="cmvg_cloud_storage_edit"),
    path('cloud_storage/delete/<int:post_id>/',views.cmvg_cloud_storage_delete,name="cmvg_cloud_storage_delete"),
    path('cloud_storage/<int:post_id>/',views.cmvg_cloud_storage_post,name="cmvg_cloud_storage_post"),
    
    path('gallery/',views.cmvg_gallery,name="cmvg_gallery"),
    path('gallery/create/',views.cmvg_gallery_create,name="cmvg_gallery_create"),
    path('gallery/edit/<int:post_id>/',views.cmvg_gallery_edit,name="cmvg_gallery_edit"),
    path('gallery/<int:post_id>/',views.cmvg_gallery_post,name='cmvg_gallery_post'),
    path('gallery/delete/<int:post_id>/',views.cmvg_gallery_delete,name="cmvg_gallery_delete"),
    path('gallery/delete/image/<int:post_id>/<int:image_id>/',views.cmvg_gallery_delete_image,name="cmvg_gallery_delete_image"),
    path('gallery/delete/access/<int:post_id>/<int:access_id>/',views.cmvg_gallery_delete_access,name="cmvg_gallery_delete_access"),

    path('members_directory/',views.cmvg_members_directory,name="cmvg_members_directory"),
    path('profile/',views.cmvg_profile,name="cmvg_profile")
 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
