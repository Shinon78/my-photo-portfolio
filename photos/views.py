from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import PhotoPost, Post
from django.core.management import call_command
from django.http import HttpResponse

def index(request):
    posts = PhotoPost.objects.all().order_by('-created_at')
    return render(request, 'photos/index.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    return render(request, 'photos/detail.html', {'post': post})

def about(request):
    return render(request, 'photos/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'photos/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'photos/post_detail.html'

def force_migrate(request):
    try:
        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)
        return HttpResponse("<h1>大成功！サマーノートの準備が完了しました！</h1><p>管理画面に戻ってブログを保存してください。</p>")
    except Exception as e:
        return HttpResponse(f"<h1>エラーが発生しました</h1><p>{e}</p>")