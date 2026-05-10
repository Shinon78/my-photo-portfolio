from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# ▼ 追加：サイトマップ用のビューをインポート
from django.contrib.sitemaps.views import sitemap

# ▼ 追加：作成したサイトマップクラスをインポート
# （※photosアプリ内のsitemaps.pyに、PostとPhotoPost用のクラスを作成したと想定しています）
from photos.sitemaps import PostSitemap, PhotoPostSitemap

# ▼ 追加：Googleに送信するサイトマップのリスト（辞書）を作成
sitemaps = {
    'blog': PostSitemap,
    'photo': PhotoPostSitemap,
}

# Googleのロボットに「全部見てOK」と伝える命令
def robots_txt(request):
    # ▼ 改良：サイトマップのURLを追記し、クローラーに直接場所を教える
    content = "User-agent: *\nAllow: /\nSitemap: https://shinotech78.com/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")

# AdSenseの正当性を証明するコード
def ads_txt(request):
    content = "google.com, pub-8285052881088341, DIRECT, f08c47fec0942fa0"
    return HttpResponse(content, content_type="text/plain")

urlpatterns = [
    path('robots.txt', robots_txt),
    path('ads.txt', ads_txt),
    
    # ▼ 追加：サイトマップのURL設定
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    # 🔒 セキュリティ対策済みの秘密の管理画面URL
    path('shino-secret-entry/', admin.site.urls),

    # 📸 メインアプリ（photos）のURL設定にすべて委譲
    path('', include('photos.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)