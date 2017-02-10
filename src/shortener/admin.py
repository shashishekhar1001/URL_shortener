from django.contrib import admin

# Register your models here.
from .models import Shortener_URL, Customer_URL

admin.site.register(Shortener_URL)
admin.site.register(Customer_URL)
