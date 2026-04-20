from django.contrib import admin
from .models import PhotoPost, Post

# すべてのモデルを1回ずつ登録します
admin.site.register(PhotoPost)
admin.site.register(Post)
# photos/admin.py に追記
from .models import Gakuchika

admin.site.register(Gakuchika)