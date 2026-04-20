from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import PhotoPost, Post, Gakuchika

# =========================================
# ギャラリー（写真）関連
# =========================================
def index(request):
    # 写真を新しい順（降順）で取得
    posts = PhotoPost.objects.all().order_by('-created_at')
    return render(request, 'photos/index.html', {'posts': posts})

def detail(request, pk):
    # 写真の詳細を取得（存在しない場合は404エラーページを表示）
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
    # ガクチカを新しい順（降順）で取得
    gakuchika_list = Gakuchika.objects.all().order_by('-created_at')
    return render(request, 'photos/gakuchika.html', {'gakuchika_list': gakuchika_list})


# =========================================
# ブログ関連 (クラスベースビュー)
# =========================================
class PostListView(ListView):
    model = Post
    template_name = 'photos/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5               # 1ページに5記事ずつ表示
    ordering = ['-created_at']    # ★追加：ブログ一覧も新しい順に表示する

class PostDetailView(DetailView):
    model = Post
    template_name = 'photos/post_detail.html'

# =========================================
# （※もし前回追加した強制更新用の force_migrate が残っている場合は、
# ここに置いたままでも、消してしまってもどちらでも大丈夫です！）
# =========================================