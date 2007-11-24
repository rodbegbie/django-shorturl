from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^adm/', include('django.contrib.admin.urls')),
    
    (r'', include('rdbgb.redirect.urls')),
)
