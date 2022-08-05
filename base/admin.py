from django.contrib import admin
from . models import Appointment, Blog, Comment, Faq, Message, Service

# Register your models here.

admin.site.register(Message)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Appointment)
admin.site.register(Faq)


admin.site.site_header = "TimePlus Cleaning"