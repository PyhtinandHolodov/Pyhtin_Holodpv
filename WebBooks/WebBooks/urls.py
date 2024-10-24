"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from catalog import views
from django.conf.urls import url
urlpatterns = [
 path('', views.index, name='home'),
 path('admin/', admin.site.urls),
]
from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
]
urlpatterns = [
 path('', views.index, name='index'),
 path('admin/', admin.site.urls),
 url(r'^books/$', views.BookListView.as_view(), name='books'),
 url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
 url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
]
from django.urls import path, include
# Добавление URL-адреса для входа в систему
urlpatterns += [
 path('accounts/', include('django.contrib.auth.urls')),
]