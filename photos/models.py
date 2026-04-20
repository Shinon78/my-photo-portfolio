from django.db import models

# =========================================
# 1. ギャラリー（写真）用のモデル
# Nikon D3100で撮影した写真などを管理します
# =========================================
class PhotoPost(models.Model):
    title = models.CharField("タイトル", max_length=100)
    # ※Render等の本番環境で画像を消えないようにするにはCloudinary等の設定が必要です
    image = models.ImageField("画像", upload_to='photos/') 
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ギャラリー写真"
        # ★追加：常に「新しい投稿順」でデータを取り出す設定
        ordering = ['-created_at'] 

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
        # ★追加：常に「新しい記事順」でデータを取り出す設定
        ordering = ['-created_at']

# =========================================
# 3. ガクチカ（学生時代の活動）用のモデル
# 修理業務やサークル代表、IoT開発などの経験を管理します
# =========================================
class Gakuchika(models.Model):
    title = models.CharField("タイトル", max_length=100)
    period = models.CharField("期間", max_length=50)
    category = models.CharField("カテゴリー", max_length=50)
    content = models.TextField("内容")
    # ★改良：Djangoの公式ルールに則り、文字項目の空欄許可は blank=True のみに統一
    result = models.TextField("成果", blank=True) 
    created_at = models.DateTimeField("登録日", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ガクチカ"
        # ★追加：常に「新しく登録した順」でデータを取り出す設定
        ordering = ['-created_at']