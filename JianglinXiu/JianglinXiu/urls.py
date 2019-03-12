"""JianglinXiu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Blog import views as blog
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', blog.index, name='index'),
                  path('blog', blog.blog, name='blog'),
                  path('blogdetails', blog.blogdetails, name="blogdetails"),
                  path('written', blog.written, name="written"),
                  path('create', blog.create, name="create"),
                  path('atlas', blog.atlas, name='atlas'),
                  path('uploadatlas', blog.uploadatlas, name='uploadatlas'),
                  path('uploadAtlasPage', blog.uploadAtlasPage, name='uploadAtlasPage'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
