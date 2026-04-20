from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class PhotoPost(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField('写真', upload_to='photos/')
    content = models.TextField('記事の本文', blank=True)
    created_at = models.DateTimeField('投稿日時', auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
# --- ここから下にブログ用のモデルを追加！ ---

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() # 本文
    image = CloudinaryField('image', blank=True, null=True) # 記事のアイキャッチ画像
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] # 新しい記事順に並べる
    class Gakuchika(models.Model):
    title = str = models.CharField("タイトル", max_length=100)
    period = models.CharField("期間", max_length=50)
    category = models.CharField("カテゴリー", max_length=50) # 例: 技術, リーダーシップ
    content = models.TextField("内容")
    result = models.TextField("成果", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __clstr__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ガクチカ"