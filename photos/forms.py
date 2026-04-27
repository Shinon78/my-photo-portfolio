from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        # フォームとして画面に表示させる項目を指定
        fields = ('name', 'email', 'subject', 'message')
        
        # HTMLの属性（classやplaceholderなど）を追加して、見た目を整えやすくする
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'お名前'}),
            'email': forms.EmailInput(attrs={'placeholder': 'メールアドレス'}),
            'subject': forms.TextInput(attrs={'placeholder': '件名'}),
            'message': forms.Textarea(attrs={'placeholder': 'お問い合わせ内容（ご自由にどうぞ）', 'rows': 5}),
        }