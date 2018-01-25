"""blog URL Configuration."""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home)
]

urlpatterns += staticfiles_urlpatterns()
