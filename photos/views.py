from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    # ギャラリー（トップページ）
    path('', views.index, name='index'),
    
    # ギャラリー詳細
    path('photo/<int:pk>/', views.detail, name='detail'),
    
    # プロフィール（ABOUT ME）
    path('about/', views.about, name='about'),
    
    # ブログ一覧（BLOG）
    path('blog/', views.PostListView.as_view(), name='post_list'),
    
    # ブログ詳細
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # --- ガクチカ（GAKUCHIKA）【今回追加！】 ---
    path('gakuchika/', views.gakuchika_view, name='gakuchika'),
]