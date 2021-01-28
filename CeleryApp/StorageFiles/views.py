from django.db.models.query_utils import FilteredRelation
from django.http.response import HttpResponse
from .models import ClassifiedFile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FileForm
from django.db.models.functions import Now
from django.utils import timezone

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
    files = ClassifiedFile.objects.filter(owner=current_user).order_by('created')
    print(files)
    return render(request, 'StorageFiles/view_files.template.html', {
        'files': files
    })

def checker(request, file_id):
    current_user = request.user
    file_to_check = get_object_or_404(ClassifiedFile, pk=file_id)
    read_file = open(file_to_check.uploadfile.path, 'r')
    read_file_data = read_file.read()
    total_words = read_file_data.split()
    sensitivity = 0
    array1 = []
    for word in total_words:
        lower_word = word.lower()
        clean_lower_word = lower_word.strip("!@#$%^&*()_+-=<>,.?/~`")
        array1.append(clean_lower_word)
    for each in array1:
        if each == "secret":
            sensitivity += 10
        elif each == "dathena":
            sensitivity += 7
        elif each == "internal":
            sensitivity += 5
        elif each == "external":
            sensitivity += 3
        elif each == "public":
            sensitivity += 1
    read_file.close()
    file_to_update = ClassifiedFile.objects.filter(pk=file_id)
    file_to_update.update(sensitivity=sensitivity)
    file_to_update.update(updated=Now())
    
    return redirect("view_files", username=current_user)
