from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve # 追加

urlpatterns = [
    # 秘密の管理画面URL
    path('shino-secret-entry/', admin.site.urls),
    
    # メインアプリ
    path('', include('photos.urls')),

    # 本番環境（DEBUG=False）でも静的ファイルやメディアを配信するための「バックアップ配線」
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# 開発環境用の設定（念のため残す）
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)