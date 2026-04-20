from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<int:pk>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # ↓ガクチカ用の道案内を追加！
    path('gakuchika/', views.gakuchika_view, name='gakuchika'),
]