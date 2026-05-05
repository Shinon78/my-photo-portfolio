from django.db import models
from tinymce.models import HTMLField
from PIL import Image, ExifTags # 追加：画像からEXIFを読み取るためのライブラリ

class PhotoPost(models.Model):
    title = models.CharField("タイトル", max_length=100)
    image = models.ImageField("画像", upload_to='photos/') 
    
    # ▼ 追加：EXIFデータを保存するフィールド（自動取得するので手入力不要＝blank, nullを許可）
    camera_model = models.CharField("カメラ機種", max_length=100, blank=True, null=True)
    focal_length = models.CharField("焦点距離", max_length=50, blank=True, null=True)
    f_stop = models.CharField("F値", max_length=50, blank=True, null=True)
    shutter_speed = models.CharField("シャッタースピード", max_length=50, blank=True, null=True)
    iso = models.CharField("ISO感度", max_length=50, blank=True, null=True)

    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def save(self, *args, **kwargs):
        # 画像がアップロードされていて、かつカメラ機種がまだ空の場合のみ実行
        if self.image and not self.camera_model:
            try:
                # 画像を開いてEXIFデータを取得
                img = Image.open(self.image)
                exif_raw = img._getexif()
                
                if exif_raw:
                    # 数字のタグIDを分かりやすい英語名に変換
                    exif_data = {
                        ExifTags.TAGS.get(k, k): v 
                        for k, v in exif_raw.items() 
                        if k in ExifTags.TAGS
                    }

                    # 1. カメラ機種 (例: NIKON D3100)
                    if 'Model' in exif_data:
                        self.camera_model = str(exif_data['Model']).strip()
                    
                    # 2. 焦点距離 (例: 35mm)
                    if 'FocalLength' in exif_data:
                        self.focal_length = f"{int(exif_data['FocalLength'])}mm"

                    # 3. F値 (例: f/5.6)
                    if 'FNumber' in exif_data:
                        self.f_stop = f"f/{float(exif_data['FNumber']):.1f}"

                    # 4. シャッタースピード (例: 1/500)
                    if 'ExposureTime' in exif_data:
                        exp = exif_data['ExposureTime']
                        if exp < 1:
                            self.shutter_speed = f"1/{int(1/float(exp))}"
                        else:
                            self.shutter_speed = f"{float(exp)}"

                    # 5. ISO感度 (例: 400)
                    if 'ISOSpeedRatings' in exif_data:
                        self.iso = str(exif_data['ISOSpeedRatings'])
                        
            except Exception as e:
                # もしEXIFがない画像（LINEで送られた画像など）がアップロードされても
                # エラーで止まらないようにpassで流す
                pass
        
        # EXIF取得が終わったら、本来の保存処理を実行
        super().save(*args, **kwargs)

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