from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import DetailView, ListView, UpdateView


# Create your views here.
class Index(ListView):
    template_name = 'main.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id).order_by('-created')


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        return render(request, 'add.html')


class Details(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


def delete(request, pk):
    if request.method == 'POST':
        Task.objects.get(pk=pk).delete()
        return redirect('/todo')


def update(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        print(task)
        task.done = not task.done
        task.save()
        return redirect('/todo')
