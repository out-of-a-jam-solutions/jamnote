import uuid
from django.db import models

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    read_expire = models.BooleanField(default=True)
    expiration = models.DateTimeField(null=True)
