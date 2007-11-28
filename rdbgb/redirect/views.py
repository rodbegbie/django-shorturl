from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from models import *

def redirect(request, key):
    target = get_object_or_404(Target, key=key)
    
    try:
        hit = RedirectHit()
        hit.target = target
        hit.referer = request.META.get("HTTP_REFERER", "")
        hit.remote_host = request.META.get("REMOTE_ADDR", "")
	hit.remote_host = request.META.get("HTTP_X_FORWARDED_FOR", hit.remote_host)
        hit.save()
    except:
        pass
    
    return HttpResponsePermanentRedirect(target.target_url)
    
