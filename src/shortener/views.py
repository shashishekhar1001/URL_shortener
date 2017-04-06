from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from analytics.models import ClickEvent
from .models import Shortener_URL, Customer_URL
from .forms import SubmitUrlForm

# Create your views here.
def shortener_fbv(request, shortcode = None, *args, **kwargs):
    # print(args)
    # print(kwargs)
    print(shortcode)#Will print None if no arguement supplied
    obj_url = None
    qs = Shortener_URL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        ClickEvent.objects.create_event(qs[0])
        obj_url = qs[0].url
        return HttpResponseRedirect(obj_url)
    return render(request, "shortener.html", {"shortcode": obj_url})

@login_required
def home(request):
    form = SubmitUrlForm(request.POST or None)
    context = {"form":form}
    template = "home.html"
    current_site = get_current_site(request)    
    if request.method == "POST":
        if form.is_valid():
            new_url = "http://" + request.POST.get("url")
            print(new_url)
            obj, created = Shortener_URL.objects.get_or_create(url=new_url)
            if created:
                template = "success.html"
            else:
                template = "already-exists.html"
            instance, flag = Customer_URL.objects.get_or_create(customer=request.user, paid_url=obj)
            instance.save()
            context = {"obj":obj, "created":created, "current_site":current_site}                
    return render(request, template, context)


def test(request):
    current_site = get_current_site(request)
    return render(request, "test.html", {"current_site":current_site})

@login_required
def dashboard(request):
    qs = Customer_URL.objects.filter(customer=request.user)
    return render(request, "dashboard.html", {"qs":qs})