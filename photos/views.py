from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.core.management import call_command
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.models import User

# モデルとフォームのインポート
from .models import PhotoPost, Post
from .forms import InquiryForm

# ==========================================
# 通常の画面表示用ビュー
# ==========================================

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

# ==========================================
# お問い合わせフォーム用ビュー
# ==========================================

def contact_view(request):
    """
    お問い合わせ画面の表示と、送信時のデータ保存を行うビュー
    """
    if request.method == 'POST':
        # 送信ボタンが押されたとき（データを受け取る）
        form = InquiryForm(request.POST)
        if form.is_valid():
            # エラーがなければデータベースに保存
            form.save()
            # 画面に完了メッセージを渡す
            messages.success(request, 'お問い合わせを送信しました。ご連絡ありがとうございます。')
            # 二重送信を防ぐため、同じページへリダイレクト
            return redirect('contact')
    else:
        # 普通にURLにアクセスしたとき（空のフォームを表示）
        form = InquiryForm()
    
    return render(request, 'contact.html', {'form': form})

# ==========================================
# メンテナンス・緊急リセット用ビュー
# ==========================================

def force_migrate(request):
    try:
        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)
        return HttpResponse("<h1>大成功！サマーノートの準備が完了しました！</h1><p>管理画面に戻ってブログを保存してください。</p>")
    except Exception as e:
        return HttpResponse(f"<h1>エラーが発生しました</h1><p>{e}</p>")

def emergency_reset_db(request):
    # ⚠️ これは緊急時専用です！
    with connection.cursor() as cursor:
        # 古いテーブルを跡形もなく消し去ります
        cursor.execute("DROP TABLE IF EXISTS photos_post CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS photos_photopost CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS django_migrations CASCADE;")
    return HttpResponse("データベースのリセットが完了しました。もう一度デプロイしてください。")

def create_admin_user(request):
    # 重複していたものを1つにまとめました
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'shino777')
        return HttpResponse("管理者ユーザー 'admin' を作成しました。")
    return HttpResponse("ユーザーは既に存在します。")

def robots_txt(request):
    text = "User-agent: *\nAllow: /\n"
    return HttpResponse(text, content_type="text/plain")