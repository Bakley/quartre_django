from django.db import models
import uuid


class RegisterEndpointModel(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    class Meta:
        ordering = ['username']
