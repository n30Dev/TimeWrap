from django.shortcuts import render
from todo.models import Task
from django.http.response import HttpResponse


def index(request):
    tasks = Task.objects.filter(user_id=request.user.id).order_by('-created')
    count = tasks.count()
    tasks = tasks[:5]
    return render(request, 'index.html', context={'tasks': tasks, 'count': count})


def schedule(request):
    return HttpResponse('schedule')


def mindmap(request):
    return HttpResponse('mindmap')


def calendar(request):
    return HttpResponse('calendar')


def notes(request):
    return HttpResponse('notes')


def lists(request):
    return HttpResponse('lists')


def dia(request):
    return HttpResponse('dia')
