from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

class PhotoPost(models.Model):
    title = models.CharField("タイトル", max_length=100)
    image = models.ImageField("画像", upload_to='photos/') 
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title

    # 修正箇所：'photos:detail' に変更
    def get_absolute_url(self):
        return reverse('photos:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "ギャラリー写真"
        ordering = ['-created_at'] 

class Post(models.Model):
    title = models.CharField("タイトル", max_length=200)
    image = models.ImageField("メイン画像", upload_to='blog_images/', blank=True, null=True)
    content = HTMLField("本文")
    views = models.PositiveIntegerField("閲覧数", default=0)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title

    # 修正箇所：'photos:post_detail' に変更
    def get_absolute_url(self):
        return reverse('photos:post_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "ブログ記事"
        ordering = ['-created_at']

class Inquiry(models.Model):
    name = models.CharField("お名前", max_length=100)
    email = models.EmailField("メールアドレス")
    subject = models.CharField("件名", max_length=200)
    message = models.TextField("お問い合わせ内容")
    created_at = models.DateTimeField("送信日", auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"

    class Meta:
        verbose_name_plural = "お問い合わせ"
        ordering = ['-created_at']