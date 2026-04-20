from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# =========================================
# プロジェクト全体のURLルート（大元の道案内）
# =========================================
urlpatterns = [
    # 🔒 セキュリティ対策済みの秘密の管理画面URL
    path('shino-secret-entry/', admin.site.urls),
    
    # 📸 メインアプリ（photos）のURL設定にすべて委譲
    # （ここで photos/urls.py に繋がり、GAKUCHIKAなども読み込まれます）
    path('', include('photos.urls')),
]

# =========================================
# 開発環境（自分のPC）専用の設定
# =========================================
# ※ 本番環境（Render）では、デザインはWhiteNoise、画像はCloudinaryが
#   自動で担当するため、このブロックはPCでのテスト時のみ動きます。
if settings.DEBUG:
    # ユーザーがアップロードした画像（メディアファイル）の表示設定
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # デザインファイル（静的ファイル）の表示設定
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)