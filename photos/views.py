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