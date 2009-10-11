from django.conf.urls.defaults import *

urlpatterns = patterns('',)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$',             'direct_to_template', {'template': 'index.html'}),
    (r'^robots.txt$',   'direct_to_template', {'template': 'robots.txt'}),   
)

urlpatterns += patterns('rdbgb.redirect.views',
    (r'^create_a_new_redirect$', 'new_redirect'),    
    (r'^(?P<key>[a-zA-Z0-9]{1,10})[\,\)]*[\./]', 'redirect'),    
)
