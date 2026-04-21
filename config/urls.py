from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔒 セキュリティ対策済みの秘密の管理画面URL
    path('shino-secret-entry/', admin.site.urls),

    # 📸 メインアプリ（photos）のURL設定にすべて委譲
    path('', include('photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)