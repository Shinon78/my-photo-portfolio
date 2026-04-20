from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import PhotoPost, Post, Gakuchika

# --- ギャラリー（写真） ---
def index(request):
    posts = PhotoPost.objects.order_by('-created_at')
    return render(request, 'photos/index.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    return render(request, 'photos/detail.html', {'post': post})

# --- プロフィール ---
def about(request):
    return render(request, 'photos/about.html')

# --- ガクチカ（今回追加！） ---
def gakuchika_view(request):
    gakuchika_list = Gakuchika.objects.order_by('-created_at')
    return render(request, 'photos/gakuchika.html', {'gakuchika_list': gakuchika_list})

# --- ブログ ---
class PostListView(ListView):
    model = Post
    template_name = 'photos/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'photos/post_detail.html'