from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls={
        'List':'/api/tasks/',
        'Detail':'/api/tasks/<int:id>/',
        'Create':'/api/tasks/create/',
        'Update':'/api/tasks/<int:id>/update/',
        'Delete':'/api/tasks/<int:id>/delete/',

    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item succesfully deleted!')