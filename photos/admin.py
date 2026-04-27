from django.contrib import admin
from .models import PhotoPost, Post, Inquiry

@admin.register(PhotoPost)
class PhotoPostAdmin(admin.ModelAdmin):
    # 写真一覧でタイトルと投稿日を表示
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 記事一覧でタイトルと投稿日を表示
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    # お問い合わせ一覧で見たい項目
    list_display = ('subject', 'name', 'email', 'created_at')
    
    # 右側に日付での絞り込みメニューを表示
    list_filter = ('created_at',)
    
    # 名前、メール、件名、内容から検索可能にする
    search_fields = ('name', 'email', 'subject', 'message')
    
    # 届いた内容は変更できないよう、すべて読み取り専用に設定
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    # 管理画面から手動でお問い合わせを追加できないようにする
    def has_add_permission(self, request):
        return False