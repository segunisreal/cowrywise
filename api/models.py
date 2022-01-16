import uuid as uuid
from django.db import models


class RandomUUID(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{uuid}"
    
    class Meta:
        ordering = ('-created_on', )


