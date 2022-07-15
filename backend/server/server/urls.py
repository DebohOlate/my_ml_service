from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    re_path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns