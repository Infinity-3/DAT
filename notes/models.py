from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=1000)
    desc=models.CharField(max_length=5000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} - {self.desc}" 