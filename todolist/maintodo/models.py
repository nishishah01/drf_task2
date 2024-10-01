from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 

class todo(models.Model):
    title=models.CharField(max_length=255,blank=False)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

