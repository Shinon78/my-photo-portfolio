from django.shortcuts import render, get_object_or_404
from .models import PhotoPost

def index(request):
    posts = PhotoPost.objects.order_by('-created_at')
    return render(request, 'photos/index.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    return render(request, 'photos/detail.html', {'post': post})
def about(request):
    return render(request, 'photos/about.html')

from django.views.generic import ListView, DetailView
from .models import Post

# 記事一覧を表示するルール
class PostListView(ListView):
    model = Post
    template_name = 'photos/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5 # 1ページに5記事表示

# 記事の詳細を表示するルール
class PostDetailView(DetailView):
    model = Post
    template_name = 'photos/post_detail.html'