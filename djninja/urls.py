from django.contrib import admin
from django.urls import include, path
from tracks.views import index

from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("index/", index),
]
