from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    # 一般公開用のメインページ
    path('', views.index, name='index'),
    path('photo/<int:pk>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('privacy/', views.privacy_policy, name='privacy'),
    
    # ▼ ここにお問い合わせフォームのURLを追加しました ▼
    path('contact/', views.contact_view, name='contact'),

    # システム管理・メンテナンス用の裏口URL
    path('force-migrate-secret/', views.force_migrate, name='force_migrate'),
    path('emergency-reset-999/', views.emergency_reset_db),
    path('create-admin-shino/', views.create_admin_user),
    path('robots.txt', views.robots_txt),
]