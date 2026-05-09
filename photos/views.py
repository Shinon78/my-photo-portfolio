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
    # ▼ 追加：人気記事（ブログ）を閲覧数順に3件取得
    popular_posts = Post.objects.order_by('-views')[:3]
    
    return render(request, 'photos/index.html', {
        'posts': posts,
        'popular_posts': popular_posts, # ▼ トップページに人気記事のデータを渡す
    })

def detail(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    return render(request, 'photos/detail.html', {'post': post})

def about(request):
    return render(request, 'photos/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'photos/post_list.html'
    context_object_name = 'posts'
    # paginate_by = 5  👈 修正：ページ分割を解除し、全記事を1ページに表示するようにしました
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'photos/post_detail.html'

    # ▼ 追加：ブログ記事が開かれるたびに、閲覧数(views)を1増やす処理
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

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
            # ▼ 修正箇所：urls.pyのapp_nameに合わせて「photos:contact」に変更 ▼
            return redirect('photos:contact')
    else:
        # 普通にURLにアクセスしたとき（空のフォームを表示）
        form = InquiryForm()
    
    # ▼ 修正箇所：フォルダ構成に合わせて「photos/contact.html」に変更 ▼
    return render(request, 'photos/contact.html', {'form': form})

# ==========================================
# メンテナンス・緊急リセット用ビュー
# ==========================================

def force_migrate(request):
    # ▼ 修正：マイグレーションの衝突を避けるため、SQLで直接viewsカラムを追加する処理に変更
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            # データベースに直接命令して、viewsの箱（整数型、初期値0）を強制追加する
            cursor.execute("ALTER TABLE photos_post ADD COLUMN IF NOT EXISTS views integer DEFAULT 0;")
        return HttpResponse("<h1>大成功！viewsカラムを追加しました！</h1><p>サイトのトップページを確認してください。</p>")
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

def privacy_policy(request):
    return render(request, 'photos/privacy.html')

def ads_txt(request):
    # シノさんのAdSense専用IDが組み込まれた証明テキストです
    text = "google.com, pub-8285052881088341, DIRECT, f08c47fec0942fa0"
    return HttpResponse(text, content_type="text/plain")