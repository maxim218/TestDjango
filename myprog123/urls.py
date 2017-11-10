from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('prilogenie111.urls')),
    url(r'^my_page_second', include('prilogenie111.urls'))
]
