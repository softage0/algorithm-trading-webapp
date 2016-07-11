from django.conf.urls import url

from . import views

app_name = 'trade'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^basic_info/(?P<code>[0-9]+)$', views.basic_info, name='basic_info'),
    url(r'^chart/(?P<code>[0-9]+)$', views.chart, name='chart'),
]
