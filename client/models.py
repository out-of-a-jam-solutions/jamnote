from django.db import models

class Note(models.Model):
    text = models.TextField()
    read_expire = models.BooleanField(default=True)
    expiration = models.DateTimeField(null=True)
