from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse  # 👈 追記1

# 👈 追記2：Googleのロボットに「全部見てOK」と伝える命令
def robots_txt(request):
    content = "User-agent: *\nAllow: /"
    return HttpResponse(content, content_type="text/plain")

urlpatterns = [
    path('robots.txt', robots_txt),  # 👈 追記3：一番上に追加
    
    # 🔒 セキュリティ対策済みの秘密の管理画面URL
    path('shino-secret-entry/', admin.site.urls),

    # 📸 メインアプリ（photos）のURL設定にすべて委譲
    path('', include('photos.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)