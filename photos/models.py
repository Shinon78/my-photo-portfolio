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
    
    # TinyMCEを使用したリッチテキスト本文
    content = HTMLField("本文")
    
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ブログ記事"
        ordering = ['-created_at']

class Inquiry(models.Model):
    """
    お問い合わせ内容を保存するモデル
    """
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