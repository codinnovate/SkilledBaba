from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Tag)


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title',  'company']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Scholarship)
class Scholarship(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Company)
admin.site.register(School)