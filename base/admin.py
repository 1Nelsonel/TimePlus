from django.contrib import admin
from . models import Blog, Comment, Message, Service

# Register your models here.

admin.site.register(Message)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Comment)


admin.site.site_header = "TimePlus Cleaning"