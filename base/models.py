from django.db import models

# Create your models here.


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
