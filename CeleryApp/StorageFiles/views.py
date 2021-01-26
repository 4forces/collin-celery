from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileForm

# Create your views here.
def index(request):
    create_form = FileForm()
    if request.method == 'POST':
        uploaded_file = request.FILES['uploadfile']
        print(uploaded_file.size)
        print(uploaded_file.name)
    return render(request, 'StorageFiles/index.template.html', {
        'form': create_form
    })