from django.conf.urls import patterns, include, url

urlpatterns = patterns('order.core.views',
    (r'^$', 'index'),
    (r'^result/$', 'result'),
)
