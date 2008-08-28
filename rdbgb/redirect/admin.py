from rdbgb.redirect.models import Target, RedirectHit
from django.contrib import admin
from django import forms
                    
class TargetAdmin(admin.ModelAdmin):
    fields = ('target_url', 'key')
    list_display = ('key', 'trimmed_target_url', 'added')

admin.site.register(Target, TargetAdmin)

class RedirectHitAdmin(admin.ModelAdmin):
    list_display = ('hit_time', 'remote_host', 'target', 'trimmed_referer')

    def trimmed_referer(self, obj):
        if len(obj.referer) < 50:
            return obj.referer
        else:
            return obj.referer[:50]+"..."    
    trimmed_referer.short_description = "Referer"
    
admin.site.register(RedirectHit, RedirectHitAdmin)