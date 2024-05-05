from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import News, StreetLeader

# Create your views here.


class HomeListView(ListView):

    template_name = 'home/index.html'
    model = News
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaders'] = StreetLeader.objects.all()

        return context

    

class AttachmentDetail(TemplateView):

    template_name = 'attachment/attachment.html'
    
class NewsDetail(DetailView):

    template_name = 'news/news_detail.html'
    model = News
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')[:8]
        
        return context