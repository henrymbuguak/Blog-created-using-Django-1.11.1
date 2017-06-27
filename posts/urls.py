from django.conf.urls import url
from django.contrib import admin
from posts import views as posts_views

urlpatterns = [
    url('^$', posts_views.post_list, name='list'),
    url('^(?P<id>\d+)/$', posts_views.index, name='post_detail'),
    url('^create$', posts_views.post_create, name='create'),
    url('^(?P<id>\d+)/edit/$', posts_views.post_update, name='update'),
    url('^(?P<id>\d+)/delete/$', posts_views.post_delete, name='delete'),
]