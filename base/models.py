from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/image', null=True)
    body = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name[0:50]


class Blog(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/image', null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title[0:50]


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

class Message(models.Model):
    user = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    ptype = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    frequency = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.name[0:50]

# class Services(models.Model):
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='static/image', null=True)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-updated', '-created']

#     def __str__(self):
#         return self.title[0:50]