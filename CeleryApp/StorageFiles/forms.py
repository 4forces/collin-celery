from django import forms
from .models import ClassifiedFile

class FileForm(forms.ModelForm):
    class Meta:
        model = ClassifiedFile
        fields = ('__all__')