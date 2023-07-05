from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Task


def index(request):
    return render(request, 'ilock/index.html')


def index2(request):
    tasks = Task.objects.all()
    return render(request, 'ilock/about.html', {'title': 'Про нас', 'tasks': tasks})


