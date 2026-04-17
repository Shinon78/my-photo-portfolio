from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 秘密の管理画面URL
    path('shino-secret-entry/', admin.site.urls),
    
    # メインアプリ（photos）のURL設定を読み込みます
    path('', include('photos.urls')),
]

# 開発環境（自分のPC）で動かしている時だけ、画像ファイルを表示するための設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # 静的ファイル（デザイン）も開発環境では標準設定で読み込みます
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)