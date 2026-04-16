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
