from django.contrib import admin
from . models import Message

# Register your models here.

admin.site.register(Message)


admin.site.site_header = "TimePlus Cleaning"