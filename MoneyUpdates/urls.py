from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'MoneyUpdates Admin Page'
admin.site.site_title = 'MoneyUpdates'

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('codyofdos/', include('job.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

