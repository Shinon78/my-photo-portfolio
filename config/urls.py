"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🌟 管理画面のURLを「admin/」から推測されにくい独自の文字列に変更しました
    path('shino-secret-entry/', admin.site.urls),
    
    # 写真アプリ（photos）のURL設定を読み込みます
    path('', include('photos.urls')),
]

# 🌟 開発環境（DEBUG=True）の場合のみ、アップロードされた画像を表示するための設定を追加
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)