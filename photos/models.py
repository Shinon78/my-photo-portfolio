from django.db import models
from django_summernote.fields import SummernoteTextField

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
    content = SummernoteTextField("本文")
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ブログ記事"
        ordering = ['-created_at']