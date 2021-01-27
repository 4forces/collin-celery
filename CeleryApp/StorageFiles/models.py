import os
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class ClassifiedFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadfile = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sensitivity = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return os.path.basename(self.uploadfile.name)

    
