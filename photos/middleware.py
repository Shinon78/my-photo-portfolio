# photos/middleware.py

from django.shortcuts import redirect

class CustomDomainRedirectMiddleware:
    """
    RenderのデフォルトURLにアクセスされた場合、独自ドメインへ転送するミドルウェア
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        
        # もしアクセスされたURLに 'onrender.com' が含まれていたら
        if 'onrender.com' in host:
            # 独自ドメインの同じページへ自動転送（301 恒久的な移動）
            return redirect('https://shinotech78.com' + request.path, permanent=True)
            
        return self.get_response(request)