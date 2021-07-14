try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
