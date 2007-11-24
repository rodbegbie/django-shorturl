from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from models import *

def about(request):
    return HttpResponse("Hello, world. You're at Rod Begbie's redirection server.")

def robots(request):
    return HttpResponse("""# No robots allowed
User-agent: *
Disallow: /""")

def redirect(request, key):
    target = get_object_or_404(Target, key=key)
    
    hit = RedirectHit()
    hit.target = target
    hit.referer = request.META.get("HTTP_REFERER", "")
    hit.remote_host = request.META.get("REMOTE_ADDR", "")
    hit.save()
    
    return HttpResponsePermanentRedirect(target.target_url)
    