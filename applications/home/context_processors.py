from .models import News

def news_context_processor(request):
    latest_news = News.objects.all().order_by('-created_at')[:2]  # Obtener las últimas 5 noticias
    return {'latest_news': latest_news}