from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault, FileField
from .models import SensitiveFiles


class SensitiveFilesSerializer(serializers.ModelSerializer):
    uploadfile_name = serializers.SerializerMethodField('get_file_name')
    uploadfile_size = serializers.SerializerMethodField('get_file_size')
    class Meta:        
        model = SensitiveFiles
        fields = ("id", "uploadfile", "uploadfile_name", "uploadfile_size", "created", "updated", "sensitivity")
    
    def get_file_name(self, sensitivefiles):
        uploadfile_name = sensitivefiles.uploadfile.name
        return uploadfile_name

    def get_file_size(self, sensitivefiles):
        uploadfile_size = sensitivefiles.uploadfile.size
        return uploadfile_size
    
