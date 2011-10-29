from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^adm/', include(admin.site.urls)),
    
    (r'', include('rdbgb.redirect.urls')),
)
