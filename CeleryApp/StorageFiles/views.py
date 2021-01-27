from .models import ClassifiedFile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FileForm

# Create your views here.

def redirect_view(request):
    response = redirect('/sensitivefiles/')
    return response

def index(request):
    create_form = FileForm(request.POST, request.FILES)
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':           
            if create_form.is_valid():
                form = create_form.save(commit=False)
                form.owner = request.user
                form.save()
                messages.success(request, "File is uploaded")
                return render(request, 'StorageFiles/index.template.html', {
                    'form': create_form,
                    'username': current_user,
                })
            else:
                messages.error(request, "Form is invalid!")
                return render(request, 'StorageFiles/index.template.html', {
                    'form': create_form,
                    'username': current_user,
                })
        else:
            return render(request, 'StorageFiles/index.template.html', {
                'form': create_form,
                'username': current_user,
            })
    else:
        messages.warning(request, "Kindly login before uploading any files!")
        return render(request, 'StorageFiles/index.template.html', {
            'form': create_form,
        })
    
@login_required
def view_files(request, username):
    current_user = User.objects.get(username=username).pk
    files = ClassifiedFile.objects.filter(owner=current_user)
    return render(request, 'StorageFiles/view_files.template.html', {
        'files': files
    })
