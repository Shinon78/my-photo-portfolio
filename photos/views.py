from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# ↓★データベースを強制更新するための部品を復活！
from django.core.management import call_command
from django.http import HttpResponse

from .models import PhotoPost, Post, Gakuchika

# =========================================
# ギャラリー（写真）関連
# =========================================
def index(request):
    posts = PhotoPost.objects.all().order_by('-created_at')
    return render(request, 'photos/index.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    return render(request, 'photos/detail.html', {'post': post})

# =========================================
# プロフィール関連
# =========================================
def about(request):
    return render(request, 'photos/about.html')

# =========================================
# ガクチカ関連
# =========================================
def gakuchika_view(request):
    gakuchika_list = Gakuchika.objects.all().order_by('-created_at')
    return render(request, 'photos/gakuchika.html', {'gakuchika_list': gakuchika_list})

# =========================================
# ブログ関連 (クラスベースビュー)
# =========================================
class PostListView(ListView):
    model = Post
    template_name = 'photos/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'photos/post_detail.html'

# =========================================
# メンテナンス用（データベース強制更新）★復活！
# =========================================
def force_migrate(request):
    try:
        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)
        return HttpResponse("<h1>大成功！データベースの更新が完了しました！</h1><p>これでガクチカが保存できるようになりました。この画面を閉じて、管理画面に戻ってください。</p>")
    except Exception as e:
        return HttpResponse(f"<h1>エラーが発生しました</h1><p>{e}</p>")