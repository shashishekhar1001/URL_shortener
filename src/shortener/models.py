import random
import string
from django.db import models

# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    # new_code = ''
    # for _ in range(size):
    #     new_code.join(random.choice(chars))
    # return new_code

class Shortener_URL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=22, unique=True)
    updated = models.DateTimeField(auto_now=True)  #Everytime the model was saved
    timestamp= models.DateTimeField(auto_now_add=True) #Everytime the model was created

    def save(self, *args, **kwargs):
        print("Everytime Something gets saved this prints")
        self.shortcode = code_generator()
        super(Shortener_URL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url) 