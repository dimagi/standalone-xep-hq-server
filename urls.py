from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^xep/', include('xep_hq_server.urls')),
    (r'^HQ/', 'example_hq.views.index'),
)
