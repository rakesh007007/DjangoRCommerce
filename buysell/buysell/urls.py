"""mysite URL Configuration

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
from buyold import views
from django.contrib.staticfiles.urls import *
from buysell.settings import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^register', views.register),
	url(r'^login', views.login),
    url(r'^main', views.main),
	url(r'^logPost', views.logPost),
    url(r'^productView', views.productView),
	url(r'^regPost', views.regPost),
    url(r'^logout', views.logout),
    url(r'^addItemPost', views.addItemPost),
    url(r'^removeItemPost', views.removeItemPost),
    url(r'^cart', views.cart),
    url(r'^addProduct', views.addProduct),
    url(r'^productPost', views.productPost),   

]
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
