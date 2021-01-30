from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from .serializers import SensitiveFilesSerializer
from .models import SensitiveFiles
# Create your views here.

@api_view(['GET'])
def apiMenu(request):
    api_urls = {
        'Menu': '/api-list/',
        'File Info': 'api-detail/<str:pk>/',
        'Create': 'api-create/',
        'Update': 'api-update/<str:pk>/',
        'Delete': 'api-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def apiList(request):
    all_files = SensitiveFiles.objects.all()
    serializer = SensitiveFilesSerializer(all_files, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiDetail(request, pk):
    single_file = SensitiveFiles.objects.get(id=pk)
    serializer = SensitiveFilesSerializer(single_file, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def apiCreate(request):
    parser_classes(MultiPartParser,)
    serializer = SensitiveFilesSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def apiDelete(request, pk):
    delete_file = SensitiveFiles.objects.get(id=pk)
    delete_file.delete()
    return Response("File record Deleted! ")
