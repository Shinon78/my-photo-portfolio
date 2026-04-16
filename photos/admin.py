from django.contrib import admin
from .models import PhotoPost

# PhotoPost（写真記事）を管理画面に登録する
admin.site.register(PhotoPost)