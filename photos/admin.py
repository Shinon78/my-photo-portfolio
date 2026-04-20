from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PhotoPost, Post

admin.site.register(PhotoPost)
admin.site.register(Post, PostAdmin)