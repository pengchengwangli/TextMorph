"""
URL configuration for TextMorph project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler400
# from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from TextMorph import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'), name='api'),
    path('',views.index, name='index'),
    path('index/',views.index),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]
handler404 = 'TextMorph.views.page_not_found'
handler500 = 'TextMorph.views.page_error'
