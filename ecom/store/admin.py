from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Catagory)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)