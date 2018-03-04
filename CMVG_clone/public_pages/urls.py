from django.urls import path

from . import views

app_name = 'public'

urlpatterns = [
    path('',views.about_us,name='index'),
    path('about_us/',views.about_us,name='about_us'),
    path('announcements/',views.announcements,name='announcements'),
    path('announcements/<int:post_id>/',views.announcements_post,name='announcements_post'),
    path('event_gallery/',views.event_gallery,name='event_gallery'),
    path('volunteers/',views.volunteers,name='volunteers'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('register/',views.register,name='register'),
    path('login/',views.login2,name="login2"),
]