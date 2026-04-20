from django.db import models

# =========================================
# 1. ギャラリー（写真）用のモデル
# Nikon D3100で撮影した写真などを管理します
# =========================================
class PhotoPost(models.Model):
    title = models.CharField("タイトル", max_length=100)
    # ※もしCloudinaryを使っている場合は models.ImageField を CloudinaryField('image') に書き換えてください
    image = models.ImageField("画像", upload_to='photos/') 
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ギャラリー写真"

# =========================================
# 2. ブログ用のモデル
# 日々の活動や技術的な備忘録を管理します
# =========================================
class Post(models.Model):
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ブログ記事"

# =========================================
# 3. ガクチカ（学生時代の活動）用のモデル 【新機能】
# 修理業務やサークル代表、IoT開発などの経験を管理します
# =========================================
class Gakuchika(models.Model):
    title = models.CharField("タイトル", max_length=100)
    period = models.CharField("期間", max_length=50)
    category = models.CharField("カテゴリー", max_length=50)
    content = models.TextField("内容")
    result = models.TextField("成果", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ガクチカ"