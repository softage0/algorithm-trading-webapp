from django.conf.urls import url

from . import views

app_name = 'kiwoom'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account_info/$', views.account_info, name='account_info'),
    url(r'^stock_list/$', views.stock_list, name='stock_list'),
    url(r'^stock_list/(?P<market_type>[0-9]+)$', views.stock_detail_list, name='stock_detail_list'),
    url(r'^basic_info/(?P<code>\w+)$', views.basic_info, name='basic_info'),
    url(r'^chart/(?P<code>\w+)$', views.chart, name='chart'),
    url(r'^api_docs/$', views.api_docs, name='api_docs'),
]
