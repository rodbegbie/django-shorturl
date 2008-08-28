from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^adm/(.*)', admin.site.root),
    
    (r'', include('rdbgb.redirect.urls')),
)
