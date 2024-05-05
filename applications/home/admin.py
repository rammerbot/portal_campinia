from django.contrib import admin

from .models import News, StreetLeader, Contact, Attachment

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'photo', 'slug']
    fields = ['title', 'description', 'photo']

    def save_model(self, request, obj, form, change):
        if not obj.author_id:  # Si no se ha asignado un autor
            obj.author = request.user  # Asignar el usuario actual
        super().save_model(request, obj, form, change)

admin.site.register(News, NewsAdmin)
admin.site.register(StreetLeader)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'phone', 'street', 'message']
admin.site.register(Contact,ContactAdmin)

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'author', 'photo', 'slug']
    fields = ['title', 'description', 'date', 'photo']

    def save_model(self, request, obj, form, change):
        if not obj.author_id:  # Si no se ha asignado un autor
            obj.author = request.user  # Asignar el usuario actual
        super().save_model(request, obj, form, change)

admin.site.register(Attachment, AttachmentAdmin)