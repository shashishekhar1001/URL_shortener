from django.shortcuts import render
from .models import Shortener_URL 

# Create your views here.
def shortener_fbv(request, shortcode = None, *args, **kwargs):
    # print(args)
    # print(kwargs)
    print(shortcode)#Will print None if no arguement supplied
    obj_url = None
    qs = Shortener_URL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj_url = qs[0].url
    
    return render(request, "shortener.html", {"shortcode": obj_url})