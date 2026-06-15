from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown_to_html')
def markdown_to_html(text):
    # extensions=[...] を入れることで、見出しやリストなど多彩な表現に対応します
    html = markdown.markdown(text, extensions=['extra'])
    return mark_safe(html)