from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


def file_dir_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class ClassifiedFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadfile = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['txt'])], upload_to=file_dir_path)
    size = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sensitivity = models.SmallIntegerField(default=0)
    
    
    
    def __str__(self):
        return self.title
