from django.db import models
from random import choice

class Target(models.Model):
    """URL to be redirected to"""
    
    key = models.CharField(maxlength=10, primary_key=True)
    target_url = models.URLField(verify_exists=True, unique=True, core=True, db_index=True)
    added = models.DateTimeField(auto_now_add=True, editable=False)

    class Admin:
        list_display = ('key', 'trimmed_target_url', 'added')
        #search_fields = ('',)
    
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

    def save(self):
        if self.key:
            super(Target, self).save() # Call the "real" save() method.
        else:            
            added = False
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            while (not added):
                self.key = choice(chars) + choice(chars) + choice(chars)
                try:
                    super(Target, self).save() # Call the "real" save() method.
                    added = True
                except django.db.IntegrityError:
                    added = False
    

class RedirectHit(models.Model):
    """Track hits to the redirect service"""
    target = models.ForeignKey(Target)
    hit_time = models.DateTimeField(auto_now_add=True, editable=False)
    referer = models.URLField(blank=True, verify_exists=False)
    remote_host = models.IPAddressField(blank=True)

    class Admin:
        list_display = ('hit_time', 'remote_host', 'target', 'trimmed_referer')
        #search_fields = ('',)

    def __str__(self):
        return "RedirectHit"

    def trimmed_referer(self):
        if len(self.referer) < 50:
            return self.referer
        else:
            return self.referer[:50]+"..."    
    trimmed_referer.short_description = "Referer"

