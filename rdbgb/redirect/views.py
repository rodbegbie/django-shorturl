from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
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

def new_redirect(request):
    user = authenticate(username=request.GET.get("username"), password=request.GET.get("password"))
    if user:
        t = Target.objects.get_or_create(target_url = request.GET.get("url"))[0]
	t.save()
	return HttpResponse("http://%s/%s" % (Site.objects.get_current().domain, t.key),mimetype="text/plain")
    else:
        raise Http404
