from django.db import models
import datetime
from random import choice

# Create your models here.
class Target(models.Model):
    """URL to be redirected to"""
    
    key = models.CharField(maxlength=10, primary_key=True)
    target_url = models.URLField(verify_exists=True, unique=True, core=True, db_index=True)
    added = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    class Admin:
        list_display = ('key', 'target_url', 'added')
        #search_fields = ('',)

    def __str__(self):
        return "Target: %s (%s)" % (self.key, self.target_url)

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
    hit_time = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    referer = models.URLField(blank=True, verify_exists=False)
    remote_host = models.IPAddressField(blank=True)

    class Admin:
        list_display = ('hit_time', 'remote_host', 'target', 'referer')
        #search_fields = ('',)

    def __str__(self):
        return "RedirectHit"
