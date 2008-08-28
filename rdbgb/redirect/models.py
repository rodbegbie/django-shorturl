from django.db import models
from random import choice

def new_key():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return choice(chars) + choice(chars) + choice(chars)

class Target(models.Model):
    """URL to be redirected to"""
    
    key = models.CharField(max_length=10, primary_key=True, default=new_key)
    target_url = models.URLField(verify_exists=True, unique=True, db_index=True)
    added = models.DateTimeField(auto_now_add=True, editable=False)

    def trimmed_target_url(self):
        if len(self.target_url) < 50:
            return self.target_url
        else:
            return self.target_url[:50]+"..."    
    trimmed_target_url.short_description = "Target URL"
    
    class Meta:
        ordering = ('-added',)

    def __str__(self):
        return "[%s] %s" % (self.key, self.trimmed_target_url())
    

class RedirectHit(models.Model):
    """Track hits to the redirect service"""
    target = models.ForeignKey(Target)
    hit_time = models.DateTimeField(auto_now_add=True, editable=False)
    referer = models.URLField(blank=True, verify_exists=False)
    remote_host = models.IPAddressField(blank=True)

    def __str__(self):
        return "RedirectHit"


