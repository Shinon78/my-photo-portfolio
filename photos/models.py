from django.db import models
from tinymce.models import HTMLField

class PhotoPost(models.Model):
    title = models.CharField("タイトル", max_length=100)
    image = models.ImageField("画像", upload_to='photos/') 
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ギャラリー写真"
        ordering = ['-created_at'] 

class Post(models.Model):
    title = models.CharField("タイトル", max_length=200)
    image = models.ImageField("メイン画像", upload_to='blog_images/', blank=True, null=True)
    
    # TextFieldからHTMLFieldに変更し、リッチテキスト編集を可能にします
    content = HTMLField("本文")
    
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ブログ記事"
        ordering = ['-created_at']