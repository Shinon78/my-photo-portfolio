from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import PhotoPost, Post

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