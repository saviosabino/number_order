from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('order.views',
    (r'^$', 'index'),
    (r'^result/$', 'result'),
)
