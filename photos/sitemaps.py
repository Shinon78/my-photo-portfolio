from django.contrib.sitemaps import Sitemap
from .models import Post, PhotoPost

# ブログ記事（Post）用のサイトマップ
class PostSitemap(Sitemap):
    changefreq = "weekly"  # 更新頻度（週1回程度）
    priority = 0.8         # 優先度

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

# ギャラリー写真（PhotoPost）用のサイトマップ
class PhotoPostSitemap(Sitemap):
    changefreq = "monthly"  # 更新頻度（月1回程度）
    priority = 0.6          # ブログより少し優先度を下げる

    def items(self):
        return PhotoPost.objects.all()

    def lastmod(self, obj):
        return obj.updated_at