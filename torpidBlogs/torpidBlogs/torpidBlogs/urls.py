from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from posts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Homepage),

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
