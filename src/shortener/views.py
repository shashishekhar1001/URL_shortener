from django.shortcuts import render

# Create your views here.
def shortener_fbv(request, shortcode = None, *args, **kwargs):
    # print(args)
    # print(kwargs)
    print(shortcode)#Will print None if no arguement supplied
    return render(request, "shortener.html", {"shortcode": shortcode})