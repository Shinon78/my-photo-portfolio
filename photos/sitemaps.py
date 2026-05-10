from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):
    changefreq = "weekly"  # 更新頻度の目安
    priority = 0.8        # 優先度（0.0〜1.0）

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # モデルに更新日フィールドがある場合