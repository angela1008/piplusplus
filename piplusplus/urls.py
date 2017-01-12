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
    url(r'^$', views.index),
    
    url(r'^login/$', apiViews.login),
    url(r'^logout/$', apiViews.logout),
    url(r'^signup/$', apiViews.signup),
    
    url(r'^front/$', apiViews.front, name='own_front'),
    url(r'^computerfront/$', apiViews.computer_front, name='own_computer_front'),
    url(r'^buildfront/$', apiViews.build_front, name='own_build_front'),
    url(r'^mathfront/$', apiViews.math_front, name='own_math_front'),
    url(r'^healingfront/$', apiViews.healing_front, name='own_healing_front'),
    url(r'^naturefront/$', apiViews.nature_front, name='own_nature_front'),
    url(r'^artfront/$', apiViews.art_front, name='own_art_front'),
    url(r'^societyfront/$', apiViews.society_front, name='own_society_front'),
    url(r'^managefront/$', apiViews.manage_front, name='own_manage_front'),
    url(r'^languagefront/$', apiViews.language_front, name='own_language_front'),
    url(r'^sportfront/$', apiViews.sport_front, name='own_sport_front'),
    url(r'^qulificationfront/$', apiViews.qulification_front, name='own_qulification_front'),
    url(r'^testfront/$', apiViews.test_front, name='own_test_front'),
    url(r'^otherfront/$', apiViews.other_front, name='own_other_front'),
    
    url(r'^profile/(?P<user>\w+)$', apiViews.profile, name='own_profile'),
    url(r'^group/$', apiViews.group, name='own_group'),
)
