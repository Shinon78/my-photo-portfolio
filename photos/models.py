from django.db import models
from django.urls import reverse  # 追加：URLを逆引きするために必要
from tinymce.models import HTMLField

class PhotoPost(models.Model):
    title = models.CharField("タイトル", max_length=100)
    image = models.ImageField("画像", upload_to='photos/') 
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)  # 追加：サイトマップで最新状態を伝えるため

    def __str__(self):
        return self.title

    # 追加：サイトマップ生成に必須（自分自身のURLを返す）
    def get_absolute_url(self):
        # 'photo_detail'の部分は、urls.pyで定義している名前に合わせてください
        return reverse('photo_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "ギャラリー写真"
        ordering = ['-created_at'] 

class Post(models.Model):
    title = models.CharField("タイトル", max_length=200)
    image = models.ImageField("メイン画像", upload_to='blog_images/', blank=True, null=True)
    
    # TinyMCEを使用したリッチテキスト本文
    content = HTMLField("本文")
    
    # ▼ 追加：人気記事表示のための閲覧数カウント
    views = models.PositiveIntegerField("閲覧数", default=0)
    
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)  # 追加：サイトマップで最新状態を伝えるため

    def __str__(self):
        return self.title

    # 追加：サイトマップ生成に必須（自分自身のURLを返す）
    def get_absolute_url(self):
        # 'blog_detail'の部分は、urls.pyで定義している名前に合わせてください
        return reverse('blog_detail', kwargs={'pk': self.pk})

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

    # お問い合わせフォームは検索エンジンにインデックスさせるページではないため、
    # get_absolute_url や updated_at は不要です。

    def __str__(self):
        return f"{self.subject} - {self.name}"

    class Meta:
        verbose_name_plural = "お問い合わせ"
        ordering = ['-created_at']