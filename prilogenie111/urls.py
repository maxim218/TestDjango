from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_page_first, name='my_page_first'),
    url(r'^my_page_second', views.my_page_second, name='my_page_second')
]
