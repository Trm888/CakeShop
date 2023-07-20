from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

urlpatterns = [
    path('', render, kwargs={'template_name': 'index.html'}, name='start_page'),
    path('admin/', admin.site.urls),
    path('api/', include('src.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
