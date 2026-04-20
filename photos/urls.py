from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<int:pk>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('gakuchika/', views.gakuchika_view, name='gakuchika'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # 👇 ここが重要！一番左の「#」を消して有効化します！
    path('force-migrate-secret/', views.force_migrate, name='force_migrate'),
]