from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
]