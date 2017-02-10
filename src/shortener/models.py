
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.
from .utils import create_shortcode
from .validators import validate_url, dot_com_validator

# Model Manager for model Shortener_URL which overrides all() method to return a query string that conatins only active=True
class Shortener_URLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(Shortener_URLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = Shortener_URL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New Codes generated:- {i}".format(i=new_codes)

class Shortener_URL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=22, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  #Everytime the model was saved
    timestamp= models.DateTimeField(auto_now_add=True) #Everytime the model was created
    active = models.BooleanField(default=False)

    #Model manager overriden
    objects = Shortener_URLManager()

    def save(self, *args, **kwargs):
        if self.shortcode == "" or self.shortcode is None:
            self.shortcode = create_shortcode(self)
        super(Shortener_URL, self).save(*args, **kwargs)
    
    def get_short_url(self):
        urlpath = reverse("scode", kwargs={"shortcode":self.shortcode})
        return "localhost:8080" + urlpath 

    def __str__(self):
        return str(self.url) 



class Customer_URL(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_url = models.ForeignKey(Shortener_URL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    # clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.customer.email