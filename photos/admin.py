from django.contrib import admin
from .models import PhotoPost

# PhotoPost（写真記事）を管理画面に登録する
admin.site.register(PhotoPost)

from django.contrib import admin
from .models import PhotoPost, Post # Postを追加

admin.site.register(PhotoPost)
admin.site.register(Post) # これで管理画面に「Posts」が現れます