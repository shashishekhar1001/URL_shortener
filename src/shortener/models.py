
from django.db import models

# Create your models here.
from .utils import create_shortcode

class Shortener_URL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=22, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  #Everytime the model was saved
    timestamp= models.DateTimeField(auto_now_add=True) #Everytime the model was created

    def save(self, *args, **kwargs):
        if self.shortcode == "" or self.shortcode is None:
            self.shortcode = create_shortcode(self)
        super(Shortener_URL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url) 