from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^admin/',admin.site.urls),
    url('^$',views.homepage,name='homepage'),
    url('^calculate/',views.calculate,name='calculate'),
    url('^check/',views.check,name='check'),
]
