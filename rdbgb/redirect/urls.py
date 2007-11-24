from django.conf.urls.defaults import *

urlpatterns = patterns('rdbgb.redirect.views',
    (r'^$', 'about'),
    (r'^robots.txt$', 'robots'),
    (r'^(?P<key>[a-zA-Z0-9]{1,10})/', 'redirect'),    
)


