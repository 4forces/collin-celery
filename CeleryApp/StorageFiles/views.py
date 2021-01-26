from django.core.files.base import File
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .forms import FileForm

# Create your views here.

def redirect_view(request):
    response = redirect('/sensitivefiles/')
    return response

def index(request):
    create_form = FileForm(request.POST, request.FILES)
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['uploadfile']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    #         if create_form.is_valid():
    #             new_upload = create_form.save(commit=False)
    #             uploaded_file = request.FILES['uploadfile']
    #             title = uploaded_file.name
    #             print(title)
    #             new_upload.title = uploaded_file.name
    #             new_upload.uploadfile = request.FILES['uploadfile']
    #             new_upload.size = uploaded_file.size
    #             new_upload.sensitivity = 0
    #             new_upload.save()
    #             print("file saved!")
    #             messages.success(request, "File is uploaded")
    #         else:
    #             messages.error(request, "Form is invalid!")
    #             return render(request, 'StorageFiles/index.template.html', {
    #                 'form': create_form
    #             })
    # else:
    #     messages.warning(request, "Kindly login before uploading any files!")
    #     return render(request, 'StorageFiles/index.template.html', {
    #         'form': create_form
    #     })
    
    return render(request, 'StorageFiles/index.template.html', {
        'form': create_form,
        'context': context,
    })
