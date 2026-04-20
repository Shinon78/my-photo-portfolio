from django.contrib import admin

# 使うモデル（設計図）をここで一括で読み込みます！
from .models import PhotoPost, Post, Gakuchika

# 管理画面に登録します
admin.site.register(PhotoPost)
admin.site.register(Post)
admin.site.register(Gakuchika)