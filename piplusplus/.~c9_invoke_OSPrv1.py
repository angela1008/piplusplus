"""piplusplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
# from django.contrib.auth.views import login, logout
from django.contrib import admin
from app import views
from api import views as apiViews

## Bckended admin management
admin.autodiscover()

## Nest-structure
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', apiViews.login),
    url(r'^logout/$', apiViews.logout),
    url(r'^signup/$', apiViews.signup),
    url(r'^index/$', views.index),
    url(r'^front/', views.front, name='user_front'),
    url(r'^profile/$', views.profile, name='user_profile'),
    url(r'^group/$', views.group),
)
