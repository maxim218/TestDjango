from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_page_first, name='my_page_first'),
    url(r'^my_page_second/(?P<pk>\d+)/$', views.my_page_second, name='my_page_second'),
    url(r'^my_page_third/', views.my_page_third, name='my_page_third'),
    url(r'^my_summa/', views.my_summa, name='my_summa'),
]
