from django.db import models

# Create your models here.
from shortener.models import Shortener_URL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, Shortener_URL):
            obj, created = self.get_or_create(shortener_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None 

class ClickEvent(models.Model):
    shortener_url = models.OneToOneField(Shortener_URL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)  #Everytime the model was saved
    timestamp= models.DateTimeField(auto_now_add=True) #Everytime the model was created

    objects = ClickEventManager()

    def __str__(self):
        return str(self.shortener_url) 
