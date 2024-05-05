from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from django.views.generic import ListView, TemplateView, DetailView
from .models import News, StreetLeader, Attachment
from .forms import ContactForm

# Create your views here.


class HomeListView(ListView):

    template_name = 'home/index.html'
    model = News
    context_object_name = 'news'
    paginate_by = 5
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaders'] = StreetLeader.objects.all()
        context['form'] = self.form_class()

        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Operación exitosa!')
            return redirect('home:home')
        else:
            # Si el formulario no es válido, vuelve a renderizar la página con el formulario y los datos existentes
            context = self.get_context_data()
            context['form'] = form
            messages.warning(request, '¡Error al enviar el Mensaje!')
            return self.render_to_response(context)
    

class Attachmentlist(ListView):

    template_name = 'attachment/attachment.html'
    model = Attachment
    context_object_name = 'attachments'


class AttachmentDetail(DetailView):

    template_name = 'attachment/attachment_detail.html'
    model = Attachment
    context_object_name = 'attachment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attachments'] = Attachment.objects.all().order_by('-created_at')[:8]
        
        return context
    
    
class NewsDetail(DetailView):

    template_name = 'news/news_detail.html'
    model = News
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')[:8]
        
        return context