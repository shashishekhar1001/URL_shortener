from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.sites.shortcuts import get_current_site

from .models import Shortener_URL 
from .forms import SubmitUrlForm

# Create your views here.
def shortener_fbv(request, shortcode = None, *args, **kwargs):
    # print(args)
    # print(kwargs)
    print(shortcode)#Will print None if no arguement supplied
    obj_url = None
    qs = Shortener_URL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj_url = qs[0].url
        return HttpResponseRedirect(obj_url)
    return render(request, "shortener.html", {"shortcode": obj_url})

def home(request):
    form = SubmitUrlForm(request.POST or None)
    context = {"form":form}
    template = "home.html"
    if request.method == "POST":
        if form.is_valid():
            new_url = "http://" + request.POST.get("url")
            print(new_url)
            obj, created = Shortener_URL.objects.get_or_create(url=new_url)
            if created:
                template = "success.html"
                context = {"obj":obj, "created":created}
            else:
                template = "already-exists.html"
                context = {"obj":obj, "created":created}                
    return render(request, template, context)


def test(request):
    return render(request, "test.html", {})