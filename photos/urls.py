from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<int:pk>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('force-migrate-secret/', views.force_migrate, name='force_migrate'),
]
path('emergency-reset-999/', views.emergency_reset_db), # 数字は適当な秘密の番号
path('create-admin-shino/', views.create_admin_user),