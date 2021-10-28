from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.date_added.date()}"
