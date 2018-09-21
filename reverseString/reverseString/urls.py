from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage,name = 'homepage'),
    url(r'reverse/', views.reverse,name = 'reverse'),
]
