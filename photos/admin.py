from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PhotoPost, Post

# ① まずここで「PostAdmin」というサマーノート用の設定を作ります
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# ② 設定を作り終わってから、最後に登録します（順番が大事です！）
admin.site.register(PhotoPost)
admin.site.register(Post, PostAdmin)