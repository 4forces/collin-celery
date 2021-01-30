from django.db import models
from django.core.validators import FileExtensionValidator
import os

# Create your models here.


class SensitiveFiles(models.Model):
    uploadfile = models.FileField(
        upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sensitivity = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return os.path.basename(self.uploadfile.name)
