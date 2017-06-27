# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "updated","timestamp"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]
    #list_display_links = ["updated"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)