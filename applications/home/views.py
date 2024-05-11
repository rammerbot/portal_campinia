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
    paginate_by = 12
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaders'] = StreetLeader.objects.all()
        context['form'] = self.form_class()
        context['news'] = News.objects.all().order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Operación exitosa!')
            return redirect('home:home')
        else:
            # en dado caso de no ser valido el form se renderiza nuevamente con los datos que tenia antes
            context = self.get_context_data()
            context['form'] = form
            messages.warning(request, '¡Error al enviar el Mensaje!')
            return self.render_to_response(context)
    
# vista de para listar los objetos del modelo attachment
class Attachmentlist(ListView):

    template_name = 'attachment/attachment.html'
    model = Attachment
    context_object_name = 'attachments'

# Vista para los detalles del los objetos del modelo Attachment
class AttachmentDetail(DetailView):

    template_name = 'attachment/attachment_detail.html'
    model = Attachment
    context_object_name = 'attachment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attachments'] = Attachment.objects.all().order_by('-created_at')[:8]
        
        return context
    
#vista para los detalles del modelo New
class NewsDetail(DetailView):

    template_name = 'news/news_detail.html'
    model = News
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')[:8]
        
        return context
    
class OrganizationView(TemplateView):
    template_name = 'organization/organization.html'