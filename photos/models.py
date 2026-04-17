from django.db import models

from django.db import models

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