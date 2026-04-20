from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    # =========================================
    # ギャラリー（写真）関連
    # =========================================
    path('', views.index, name='index'),
    path('photo/<int:pk>/', views.detail, name='detail'),

    # =========================================
    # プロフィール関連
    # =========================================
    path('about/', views.about, name='about'),

    # =========================================
    # ガクチカ関連
    # =========================================
    path('gakuchika/', views.gakuchika_view, name='gakuchika'),

    # =========================================
    # ブログ関連
    # =========================================
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # =========================================
    # メンテナンス用（⚠️セキュリティ対策）
    # =========================================
    # データベースの強制更新URLは、誰かに悪用されるのを防ぐため、
    # 役目を終えたら先頭に「#」をつけてコメントアウト（無効化）しておきます。
    # また必要になった時だけ「#」を外せばOKです！
    # path('force-migrate-secret/', views.force_migrate, name='force_migrate'),
]